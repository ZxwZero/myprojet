#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.org/
@software: PyCharm
@file: urls.py
@time: 2016/11/26 下午5:25
"""

# from django.urls import path
from django.conf.urls import include, url

from django.views.decorators.cache import cache_page
from . import views

app_name = "oauth"
urlpatterns = [
    url(r'oauth/authorize', views.authorize),
    url(r'oauth/requireemail/<int:oauthid>.html', views.RequireEmailView.as_view(), name='require_email'),
    url(r'oauth/emailconfirm/<int:id>/<sign>.html', views.emailconfirm, name='email_confirm'),
    url(r'oauth/bindsuccess/<int:oauthid>.html', views.bindsuccess, name='bindsuccess'),
    url(r'oauth/oauthlogin', views.oauthlogin, name='oauthlogin')
]
