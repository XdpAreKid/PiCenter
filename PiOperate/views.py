import os
import math

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from pyecharts import Line3D
from pyecharts.constants import DEFAULT_HOST
from django.views.generic.base import TemplateView
import plotly.offline as opy
import plotly.graph_objs as go

from .models import Applist
from .api import get_ip_address, get_release_info, get_Filesystem_info, \
    getCPUtemperature, get_system_uptime, getCPUuse, getRAMinfo



# Create your views here.
def file_views(request):
    PCILIST = Applist.objects.all()
    return render(request, 'file.html', locals())

def download_views(request):
    PCILIST = Applist.objects.all()
    return render(request, 'download.html',locals())

def jupyter_views(request):
    PCILIST = Applist.objects.all()
    ip = get_ip_address()
    return render(request, 'jupyter.html', locals())

def process_view(request):
    info = os.popen('ps aux').readlines()
    PCILIST = Applist.objects.all()
    i = 0
    process_info = list()
    for line in info:
        i += 1
        if i > 1:
            get = line.split()
            a = dict()
            a['pid'] = get[1]
            a['owner'] = get[0]
            a['command'] = get[10]
            for item in get[11:]:
                a['command'] += ' ' + item
            a['cpu'] = get[2]
            a['memory'] = get[3]
            process_info.append(a)
    process_info.sort(key=lambda k:(k.get('cpu',0)))
    process_info=process_info[1:]
    return render(request, 'process.html', locals())


def dashboard_view(request):
    PCILIST = Applist.objects.all()
    pi_info = get_release_info()
    pi_system = get_Filesystem_info()
    pi_cpu_temp = getCPUtemperature()
    uptime = get_system_uptime()
    ip = get_ip_address()
    cpu = getCPUuse()
    RAM_stats = getRAMinfo()
    RAM_total = round(int(RAM_stats[0]) / 1000, 1)
    RAM_used = round(int(RAM_stats[1]) / 1000, 1)
    RAM_free = round(int(RAM_stats[2]) / 1000, 1)
    return render(request, 'system_info.html', locals())


