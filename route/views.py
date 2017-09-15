# coding: utf-8

# Create your views here.
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from route.models import Sidebar,SidebarLevel,UserRoutingInfo,GroupRoutingInfo
from django.contrib.auth.models import Group

import json

@login_required
def get_sidebar(request):
    sidebar = Sidebar.objects.all()
    sidebar_level = SidebarLevel.objects.all()
    sidebar_dic = {}
    for side in sidebar:
        content = []
        for level in sidebar_level:
             if str(side.sidebar_name) == str(level.sidebar_name):
                 content.append([level.level_name,level.url_name])
        if content:
            sidebar_dic[str(side.sidebar_name)]=content

    print '------',sidebar_dic
    return render(request,'getsidebar.html',{'sidebar_dic':sidebar_dic})

@login_required
def get_routing_info(request):
    print '-------------',request.GET.lists
    routing = request.GET.getlist('routing')
    print routing
    routing_info = {}
    for info in routing:
        #print info
        info = info.split(':')
        sidebar = info[0]
        sidebar_level = eval(info[1])
        if not routing_info.has_key(sidebar):
            sidebar_level_list = []
            sidebar_level_list.append(sidebar_level)
            routing_info[sidebar] = sidebar_level_list
        else:
            sidebar_level_list.append(sidebar_level)
            routing_info[sidebar] = sidebar_level_list
    print routing_info
    group_name = Group.objects.get(name='testgroup')
    GroupRoutingInfo.objects.create(groupname=group_name, routing_info=json.dumps(routing_info))
    return render(request, 'getsidebar.html')


