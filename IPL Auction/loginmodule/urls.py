"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from loginmodule.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url(r'^backend/$',backend),
    url(r'^home/$',login),
    url(r'^auth/$',auth_view),
    url(r'^loggedin/$',loggedin),
    url(r'^logout/$',logout),
    url(r'^add/$',add_price),
    url(r'^refresh/$',refresh),
    url(r'^change_db/$',change_db),
    url(r'^cur_bid/$',cur_bid),
]