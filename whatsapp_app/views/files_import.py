



from django.shortcuts import render

from django.contrib.auth.models import User,auth
from django.conf import settings
from whatsapp_app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password

import random,math,os,json
from datetime import datetime, timedelta
from datetime import date

# Create your views here.


##############################  page  ##############################


def error_404(request):
    return render(request,'adminTemplate/error-404.html') 


def start(request):
    return redirect('logins')

def dashboard(request):   

    return render(request,"adminTemplate/dashboard.html")     




def header(request):        

    user_detail_obj=user_details.objects.get(user=request.user.id)
    
    owner_img=user_detail_obj.owner_img
    print(owner_img,'000000000')
    context={
        'owner_img':owner_img,
    }
    return render(request,'adminTemplate/header.html',context)


def loginuserdetail(request):
    
    try: 
         loginusername=request.session['usernames']
    except:
         loginusername=request.session['username']

    print(loginusername)

    return loginusername


