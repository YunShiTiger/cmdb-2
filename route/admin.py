from django.contrib import admin

# Register your models here.

from route.models import Sidebar,SidebarLevel,UserRoutingInfo

#class SidebarAdmin(admin.ModelAdmin):
#    list_display = ('sidebar_name')

class SidebarLevelAdmin(admin.ModelAdmin):
    list_display = ('sidebar_name','level_name','url_name','enable')

class UserRoutingInfoAdmin(admin.ModelAdmin):
    list_display = ('username','routing_info')

admin.site.register(Sidebar)
admin.site.register(SidebarLevel,SidebarLevelAdmin)
admin.site.register(UserRoutingInfo,UserRoutingInfoAdmin)