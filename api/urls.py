# -*- coding: utf-8 -*-
from . import views
from api.resources import ImportRowResource
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from api.views import list

row_resource = ImportRowResource()

urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(row_resource.urls)),
]

# # When in development env use the local MEDIA_ROOT directory to save files
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)