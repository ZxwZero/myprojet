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
@time: 2016/11/2 下午7:15
"""

# from django.urls import url
from django.conf.urls import include, url

from django.views.decorators.cache import cache_page
from . import views
from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView

app_name = "blog"
urlpatterns = [
    # url(r'', views.IndexView.as_view(), name='index'),
    url(r'^$', views.zxw_index, name='index'),
    url(r'^test$', views.test, name='test'),
    url(r'^xbb_love$', views.xbb_love, name='xbb_love'),
    url(r'page/<int:page>/', views.IndexView.as_view(), name='index_page'),

    url(r'article/<int:year>/<int:month>/<int:day>/<int:article_id>.html',
         views.ArticleDetailView.as_view(),
         name='detailbyid'),

    url(r'category/<slug:category_name>.html', views.CategoryDetailView.as_view(), name='category_detail'),
    url(r'category/<slug:category_name>/<int:page>.html', views.CategoryDetailView.as_view(),
         name='category_detail_page'),

    url(r'author/<author_name>.html', views.AuthorDetailView.as_view(), name='author_detail'),
    url(r'author/<author_name>/<int:page>.html', views.AuthorDetailView.as_view(),
         name='author_detail_page'),

    url(r'tag/<slug:tag_name>.html', views.TagDetailView.as_view(), name='tag_detail'),
    url(r'tag/<slug:tag_name>/<int:page>.html', views.TagDetailView.as_view(), name='tag_detail_page'),
    url('archives.html', views.ArchivesView.as_view(), name='archives'),
    url(r'upload', views.fileupload, name='upload'),
    url(r'refresh', views.refresh_memcache, name='refresh')
]
