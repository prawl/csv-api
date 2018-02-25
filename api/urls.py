# -*- coding: utf-8 -*-
from . import views
from api.views import list
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # TODO: Update this name to api/file/create
    url(r'^list/$', list, name='list'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/rows', views.ImportRowIndex.as_view()),
]