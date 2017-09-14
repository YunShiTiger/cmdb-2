
# Create your views here.
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from route.models import Sidebar,SidebarLevel,UserRoutingInfo

@login_required
def get_sidebar(request):
    sidebar = Sidebar.objects.all()
    sidebar_level = SidebarLevel.objects.all()
    result = []
    for side in sidebar:
        print '------',side.sidebar_name
        for level in sidebar_level:
            if str(side.sidebar_name) == str(level.sidebar_name):
                print level.url_name
    return render(request,'getsidebar.html',{'sidebar':sidebar,'sidebar_level':sidebar_level})

