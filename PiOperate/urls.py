from django.conf.urls import url
from django.contrib import admin
from .views import file_views,download_views, jupyter_views, process_view, dashboard_view
from .api import kill_process_api
from django.urls import include
from filemanager import urls


urlpatterns = [
    url(r'^filelist/$', file_views),
    url(r'^download/$', download_views),
    url(r'file/', include('filemanager.urls')),
    url(r'^jupyter/',jupyter_views),
    url(r'process/', process_view),
    url(r'dashboard/', dashboard_view,name='home'),
    url(r'kill_process', kill_process_api, name='kill_process'),
    url(r'^$',download_views),
]
