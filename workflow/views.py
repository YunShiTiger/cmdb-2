from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from asset.utils import deny_resubmit
from models import TicketType,TicketTasks,TicketOperating
from django.contrib.auth.models import User
from salt_api.api import SaltApi
from asset.models import gogroup,svn,minion,GOTemplate,goservices,gostatus
from mico.settings import svn_username,svn_password,go_local_path,go_move_path,go_revert_path,svn_gotemplate_repo,svn_gotemplate_local_path
import json
import uuid
import xmlrpclib
salt_api = SaltApi()


# Create your views here.
@login_required
@deny_resubmit(page_key='workflow_index')
def index(request):
    ticket_type = TicketType.objects.all()
    return render(request,'workflow_index.html',{'ticket_type':ticket_type})


@login_required
def get_hosts(request):
    ticket_type = request.GET['ticket_type']
    obj = TicketType.objects.get(type_name=ticket_type)
    content = []
    hosts = []
    handler = []
    for host in obj.hosts.values():
        hosts.append(host['saltname'])
    content.append(hosts)
    for info in obj.handler.values():
        handler.append(info['username'])
    content.append(handler)
    return HttpResponse(json.dumps(content))

@login_required
def my_tickets(request):
    tasks = TicketTasks.objects.filter(creator=request.user)
    return render(request,'my_tickets.html',{'tasks':tasks})



@login_required
def get_ticket_tasks(request):
    username = User.objects.get(username=request.user)
    tasks = TicketTasks.objects.filter(handler=username).filter(state='1')
    return render(request,'get_ticket_tasks.html',{'tasks':tasks})

@login_required
def submit_tickets(request):
    title = request.GET['title']
    ticket_type = request.GET['ticket_type']
    function = request.GET['function']
    hosts = request.GET.getlist('hosts')
    project = request.GET['project']
    go_command = request.GET['go_command']
    supervisor_name =  request.GET['supervisor_name']
    svn_repo = request.GET['svn_repo']
    statsd = request.GET['statsd']
    sentry = request.GET['sentry']
    handler = request.GET['handler']

    
    salt_command = {
        "title":title,
        "ticket_type":ticket_type,
        "function":function,
        "hosts":hosts,
        "project":project,
        "svn_repo":svn_repo,
        "supervisor_name":supervisor_name,
        'go_command':go_command,
        'statsd':statsd,
        'sentry':sentry,
        'handler':handler,
        'owner':str(request.user)
        }
    salt_command = json.dumps(salt_command)
  
    ticket_type = TicketType.objects.get(type_name=ticket_type)
    handler = User.objects.get(username=handler)
    task_id = str(uuid.uuid1())
    TicketTasks.objects.create(tasks_id=task_id,title=title,ticket_type=ticket_type,creator=request.user,content=salt_command,handler=handler,state='1')
    return render(request,'get_ticket_tasks.html')


@login_required
def handle_tickets(request):
    task_id = request.GET['id']
    submit = request.GET['submit']
    reply = request.GET['reply']
    operating_id = TicketTasks.objects.get(tasks_id=task_id)
    username = User.objects.get(username=request.user)
    if submit == 'reject':
        TicketTasks.objects.filter(tasks_id=task_id).update(state='4')
        TicketOperating.objects.create(operating_id=operating_id,handler=username,content=reply,result='2')
    else:
        content = TicketTasks.objects.get(tasks_id=task_id).content
        content = json.loads(content)
        for host in content['hosts']:
            data = {
                'client':'local',
                'tgt':host,
                'fun':'state.sls',
                'arg':['goservices.supervisor_submodule','pillar={"svnusername":"deploy","svnpassword":"ezbuyisthebest","goprograme":"%s","svnrepo":"%s","supProgrameName":"%s","goRunCommand":"%s"}' % (content['project'],content['svn_repo'],content['supervisor_name'],content['go_command'])]
            }
            result = salt_api.salt_cmd(data)

            minion_host = minion.objects.get(saltname=host)    
            supervisor_info = gostatus.objects.get(hostname=minion_host)
            supervisor_obj = xmlrpclib.Server('http://%s:%s@%s:%s/RPC2' % (
                supervisor_info.supervisor_username, supervisor_info.supervisor_password,
                supervisor_info.supervisor_host, supervisor_info.supervisor_port))
            
            try:
                if supervisor_obj.supervisor.getProcessInfo(content['supervisor_name']):
                    deploy_result = 1
                    print '-------successful-----'
            except Exception, e:
                print e
                deploy_result = 0
                TicketTasks.objects.filter(tasks_id=task_id).update(state='5')
                TicketOperating.objects.create(operating_id=operating_id,handler=username,content=reply,result='1')
                print '------failed-------------'           
            
            #-------------------------new project-----------------------------------
            try:
                if deploy_result == 1:
                    if gogroup.objects.filter(name=content['project']):
                        print 'The %s project is existing!!' % content['project']
                    else:
                        obj = gogroup(name=content['project'])
                        obj.save()

                        project = gogroup.objects.get(name=content['project'])
                        obj = svn(username=svn_username,
                            password=svn_password,
                            repo=content['svn_repo'],
                            localpath=go_local_path + content['project'],
                            movepath=go_move_path + content['project'],
                            revertpath=go_revert_path,
                            executefile=go_local_path + content['project'] + '/' + content['project']
                            ,project=project)
                        obj.save()


                    #-------------------------gotemplate-----------------------------------
                    project = gogroup.objects.get(name=content['project'])
                    #minion_host = minion.objects.get(saltname=host)
                    ip = minion_host.ip

                    if GOTemplate.objects.filter(hostname=minion_host).filter(project=project).filter(env=1):
                        print 'The %s gotemplate project is existing!!' % content['project']
                    else:
                        obj = GOTemplate(
                            username=svn_username,
                            password=svn_password,
                            repo=content['svn_repo'],
                            localpath=go_local_path + content['project'],
                            env=1,
                            hostname=minion_host,
                            project=project)
                        obj.save()

                    #-------------------------goservices-----------------------------------
                    if goservices.objects.filter(saltminion=minion_host).filter(group=project).filter(name=content['supervisor_name']).filter(env=1):
                        print 'The %s goservice is existing!!' % content['supervisor_name']
                    else:
                        obj = goservices(
                            ip=ip,
                            name=content['supervisor_name'] ,
                            env=1,
                            group=project,
                            saltminion=minion_host,
                            owner=content['owner'],
                            has_statsd=content['statsd'],
                            has_sentry=content['sentry'],
                            comment=content['function'])
                        obj.save()

                    TicketTasks.objects.filter(tasks_id=task_id).update(state='3')
                    TicketOperating.objects.create(operating_id=operating_id,handler=username,content=reply,result='1')
            except Exception, e:
                TicketTasks.objects.filter(tasks_id=task_id).update(state='5')
                TicketOperating.objects.create(operating_id=operating_id,handler=username,content=reply,result='1')





    return render(request,'get_ticket_tasks.html')



