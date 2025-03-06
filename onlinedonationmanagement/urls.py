"""
URL configuration for onlinedonationmanagement project.

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
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.homefunction),
    path("about", views.demofunction,name="about"),
    path("login/", views.demofunction1,name="login"),
    path("home/",views.homefunction,name="home"),
    path("contact/", views.contactfunction, name="contact"),
    path("adminlogin/",views.adminlogin,name="adminlogin"),
    path("register/", views.register, name="register"),
    path("succesfull/", views.succesfull, name="successfull"),

    path("",include("adminapp.urls")),
    # path("", include("donorapp.urls")),
    # path("", include("recipientapp.urls"))

]
