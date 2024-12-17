from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .ctl.RegistrationCtl import RegistrationCtl
from .ctl.LoginCtl import LoginCtl
from .ctl.WelcomeCtl import WelcomeCtl

@csrf_exempt
def action(request,page):
    ctlName=page+"Ctl()"
    ctlObj=eval(ctlName)
    return ctlObj.execute(request,{"id":0})

@csrf_exempt
def auth(request, page="",operation="",id=0):
    if page=="Logout":
        Session.objects.all().delete()
        request.session['user']=None
        ctlName="Login"+"Ctl()"
        ctlObj=eval(ctlName)
        res=ctlObj.execute(request,{"id":id,"operation":operation})
    return res

def index(request):
    res=render(request,'Welcome.html')
    return res