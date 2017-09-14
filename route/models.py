# coding: utf-8

from django.db import models
from django.contrib.auth.models import User

CHOICE_ENV = (
    (0, U'禁用'),
    (1, U'启用')
    )


class Sidebar(models.Model):
    sidebar_name = models.CharField(max_length=128, verbose_name=u"侧边栏名称")

    def __unicode__(self):
        return self.sidebar_name

class SidebarLevel(models.Model):
    sidebar_name = models.ForeignKey(Sidebar)
    level_name = models.CharField(max_length=128, verbose_name=u"下级名称")
    url_name = models.CharField(max_length=512, verbose_name=u"路由名称")
    enable = models.IntegerField(choices=CHOICE_ENV, blank=True, null=True, verbose_name=u"是否启用")

    def __unicode__(self):
        return self.level_name

class UserRoutingInfo(models.Model):
    username = models.OneToOneField(User)
    routing_info = models.CharField(max_length=20480)

    def __unicode__(self):
        return self.username

