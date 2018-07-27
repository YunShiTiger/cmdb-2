# coding:utf8
import json, os, sys
import re
import threading
reload(sys)
sys.setdefaultencoding('utf8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mico.settings")
import django
django.setup()

from functools import partial
from django.core.serializers import serialize
from django.core.mail import EmailMultiAlternatives, get_connection
from mico.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD,  EMAIL_USER



serialize = partial(serialize, 'json')


def id_to_dict(obj_dict, value):
    obj_dict.update(id=value)
    return obj_dict


def serialize_queryset(obj):
    obj_list = [id_to_dict(partial_item.get('fields'), partial_item.get('pk'))
                for partial_item in json.loads(serialize(obj))]
    return obj_list


def serialize_instance(obj):
    if obj:
        return serialize_queryset([obj])[0]
    else:
        return None


def cut_str(str, len):
    cut_len = r'.{%s}' % len
    str_list = re.findall(cut_len, str)
    new_str = '\n'.join(str_list)
    return new_str


class EmailThread(threading.Thread):
    def __init__(self, subject, body, from_email, recipient_list, fail_silently):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        threading.Thread.__init__(self)

    def run(self):
        conn = get_connection()
        conn.username = EMAIL_USER  # 更改用户名
        conn.password = EMAIL_HOST_PASSWORD  # 更改密码
        conn.host = EMAIL_HOST  # 设置邮件服务器
        conn.open()

        msg = EmailMultiAlternatives(self.subject, self.body, self.from_email, self.recipient_list)
        msg.attach_alternative(self.body, "text/html")
        print '*********run done'
        # msg.send(self.fail_silently)
        conn.send_messages([msg, ])
        conn.close()


def send_mail_thread(subject, body, from_email, recipient_list, fail_silently=False, *args, **kwargs):
    EmailThread(subject, body, from_email, recipient_list, fail_silently).start()

