"""pro7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from pro7 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome,name='welcome'),
    
    path('sample/',views.sample,name='sample'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('details/',views.details,name='details'),
    path('sdetails/',views.sdetails,name='sdetails'),
    path('update/<email>/',views.update,name='update'),
    path('delete/<email>/',views.delete,name='delete'),
    path('home/',views.home,name='home'),
]
