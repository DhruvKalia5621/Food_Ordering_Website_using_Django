"""
URL configuration for Food_Website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from myApp import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.loginpage,name='loginpage'),
    path('',views.Homepage,name='home'),
    path('registration/',views.registerpage,name='registerpage'),
    # path('logoutpage/',views.logoutpage,name='logout'),
    path('Home/',views.Homepage,name='Home'),
    path('login/payment/',views.paymentform,name='paymentform'),
     path('profilepage/',views.profilepage,name='profilepage'),
     path('payment/',views.paymentform,name='paymentform'),
     path('basic/',views.basicwebsite,name='basic'),

     path('logout/',views.logoutpage,name='logout'),
     
     path('practice/',views.practicepage,name='practicepage'),
     path('form/',views.form,name='formpage'),
     path('Reset/',views.Resetpassword,name='Resetpass'),
     path('changeuserpass/',views.changeuserpass,name='changeuserpass'),
     path('removeuser/',views.removeuser,name='removeuser'),
     path('uploadfile/',views.uploadfile,name='uploadfile'),
     path('sushimenu/',views.Sushimenu,name='sushimenu'),
     path('aboutus/',views.aboutus,name='aboutus'),
     path('Menu/',views.Menu,name='Menu'),
     path('Contact/',views.Contact,name='contact'),

     path('Loginform/',views.foodloginform,name='loginform'),
     
     path('Burgermenu/',views.Burgermenu,name='Burgermenu'),
     path('Pizzamenu/',views.Pizzamenu,name='Pizzamenu'),
     path('Sandwichmenu/',views.Sandwichmenu,name='Sandwichmenu'),
     path('complaints/',views.complaintstable,name='complaints'),
     path('homepage/',views.Homepage,name='homepage'),

    path('userprofile/',views.userprofile,name='userprofile'),
    path('addmobile/',views.addmobile,name='addmobile'),
    path('enterotp/',views.enterotp,name='enterotp'),
    path('Orders/',views.CustomerOrderList,name='CustomerOrderList'),
    

     
    


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
