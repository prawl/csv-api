# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/files/upload$', views.ImportFileUpload.as_view()),
    url(r'^', admin.site.urls),
    url(r'^api/rows', views.ImportRowIndex.as_view()),
]