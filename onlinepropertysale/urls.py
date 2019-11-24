"""onlinepropertysale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app1 import views
from onlinepropertysale import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('welcome/', views.welcome),
    path('home/', views.home),
    path('signup/', views.signup, name='signup'),
    path('savesignup/', views.savesignup),
    path('logout/', views.logout),
    path('adduser/', views.adduser),
    path('usersave/', views.usersave),
    path('viewuser/', views.viewuser),
    path('viewUser/', views.viewUser),
    path('changepass/', views.changepass),
    path('updateuser/', views.updateuser),
    path('delete/', views.delete),
    path('deleteuser/', views.deleteuser),
    path('about/', views.aboutus),

    path('plotreg/', views.plotreg),
    path('saveplot/', views.saveplot),
    path('viewplot/', views.viewplot),
    path('editplot/', views.editplot),
    path('editplotno/', views.editplotno),
    path('updateplotnumber/', views.updateplotnumber),
    path('updateplot/', views.updateplot),
    path('deleteplot/', views.deleteplot),

    path('appreg/', views.appartmentreg),
    path('saveappartment/', views.saveappartment),
    path('viewapp/', views.viewappartment),
    path('editapp/', views.editappartment),
    path('editappno/', views.editappno),
    path('updateappnumber/', views.updateappnumber),
    path('updateapp/', views.updateapp),
    path('deleteapp/', views.deleteapp),

    path('empreg/', views.empreg),
    path('saveemployee/', views.saveemployee),
    path('viewemp/', views.viewemp),
    path('editemp/', views.editemp),
    path('editempno/', views.editempno),
    path('updateempnumber/', views.updateempnumber),
    path('updateemp/', views.updateemp),
    path('deleteemp/', views.deleteemp)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
