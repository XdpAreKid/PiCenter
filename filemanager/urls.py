from django.conf.urls import url
from django.contrib import admin
import filemanager.views as fm

urlpatterns = [
    url(r'^$', fm.index),
    url(r'^list$', fm.list_),
    url(r'^rename$', fm.rename),
    url(r'^move$', fm.move),
    url(r'^copy$', fm.copy),
    url(r'^remove$', fm.remove),
    url(r'^edit$', fm.edit),
    url(r'^getContent$', fm.getContent),
    url(r'^createFolder$', fm.createFolder),
    url(r'^changePermissions$', fm.changePermissions),
    url(r'^compress$', fm.compress),
    url(r'^extract$', fm.extract),
    url(r'^downloadMultiple$', fm.downloadMultiple),
    url(r'^download$', fm.download),
    url(r'^upload$', fm.upload),
]
