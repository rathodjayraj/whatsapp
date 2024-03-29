from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

########## page import ########## 
from whatsapp_app.views.files_import import *
from whatsapp_app.views.login_logout import *

from whatsapp_app.views.templatelist import *



urlpatterns = [

        
    ##############################  all page  ##############################

  
    path('dashboard/', dashboard, name="dashboard"),
    path('error', error_404, name="error"),

     ##############################  login && forget  ##############################
    path('login/', logins, name="logins"),
    path('logoutpage/', logout, name="logoutpage"),
    path('send_mail', send_mails, name="send_mail"),
    path('setpwd', set_pwd, name="setpwd"),


    path('profile_page/', profile_page, name="profile_page"),
    path('profile/', profile, name="profile"),
    path('header', header, name="header"),

    path('templatelist', templatelist, name="templatelist"),
    path('contactlist', contactlist, name="contactlist"),
    path('campainlist', campainlist, name="campainlist"),



    ##############################  all super admin function  ##############################


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
