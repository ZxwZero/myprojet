#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence 
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.net/
@software: PyCharm
@file: urls.py
@time: 2018/2/25 下午3:04
"""
# from django.urls import path
from django.conf.urls import include, url

from . import views

app_name = "owntracks"

urlpatterns = [
    url('owntracks/logtracks', views.manage_owntrack_log, name='logtracks'),
    url('owntracks/show_maps', views.show_maps, name='show_maps'),
    url('owntracks/get_datas', views.get_datas, name='get_datas'),
    url('owntracks/show_dates', views.show_log_dates, name='show_dates')
]
