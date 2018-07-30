# coding:utf8
import sys, os, time, requests, datetime
reload(sys)
sys.setdefaultencoding('utf8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mico.settings")
import django
django.setup()

from django.db.models import Q
from mico.settings import EMAIL_HOST_USER, CMDB_URL
from publish import models


if __name__ == "__main__":
    print datetime.datetime.now()
    publishsheets = models.PublishSheet.objects.filter((Q(status='1') & Q(approval_level__name='1')) | Q(status='3'))
    if publishsheets:
        # 判断时间
        now_int = time.time()
        for publish in publishsheets:
            print 'publish : ', publish.id
            publish_datetime_str = publish.publish_date + ' ' + publish.publish_time
            publish_datetime_format = time.strptime(publish_datetime_str, '%Y-%m-%d %H:%M')
            publish_datetime_int = time.mktime(publish_datetime_format)
            if now_int + 240 < publish_datetime_int <= now_int + 300:
                print '5 min : ', publish.id
                # 5分钟后到达发布时间
                to_list = [publish.creator.email]
                try:
                    projectinfo_obj = models.ProjectInfo.objects.get(group=publish.goservices.all()[0].group)
                except models.ProjectInfo.DoesNotExist:
                    projectinfo_obj = None
                else:
                    if projectinfo_obj.mail_group.all():
                        to_list.extend([approver.email for approver in projectinfo_obj.mail_group.all() if approver.email])

                url = CMDB_URL + 'asset/project/send/email/'
                params = {
                    'sheet_id': publish.id,
                    'head_content': u'5分钟后即可发布',
                    'to': to_list,
                    'can_approve': '2'
                }
                r = requests.get(url, params)
                if r.status_code != 200:
                    errcode = 500
                    msg = u'邮件发送失败'

            if publish_datetime_int + 1740 < now_int <= publish_datetime_int + 1800:
                print '30 min : ', publish.id
                # 超时30未发布
                to_list = [publish.creator.email]
                try:
                    projectinfo_obj = models.ProjectInfo.objects.get(group=publish.goservices.all()[0].group)
                except models.ProjectInfo.DoesNotExist:
                    projectinfo_obj = None
                else:
                    if projectinfo_obj.mail_group.all():
                        to_list.extend([approver.email for approver in projectinfo_obj.mail_group.all() if approver.email])

                url = CMDB_URL + 'asset/project/send/email/'
                params = {
                    'sheet_id': publish.id,
                    'head_content': u'发布单已超时30分钟，请尽快发布',
                    'to': to_list,
                    'can_approve': '2'
                }
                r = requests.get(url, params)
                if r.status_code != 200:
                    errcode = 500
                    msg = u'邮件发送失败'

    url = CMDB_URL + 'asset/project/send/email/'
    params = {
        'sheet_id': 1,
        'head_content': u'发布单已超时30分钟，请尽快发布',
        'to': ['huangyao@ezbuy.com'],
        'can_approve': '2'
    }
    r = requests.get(url, params)
    if r.status_code != 200:
        errcode = 500
        msg = u'邮件发送失败'
