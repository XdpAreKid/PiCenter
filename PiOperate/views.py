from django.shortcuts import render
from .models import Applist
import os

# Create your views here.
def file_views(request):
    PCILIST = Applist.objects.all()
    return render(request, 'file.html', locals())

def download_views(request):
    PCILIST = Applist.objects.all()
    return render(request, 'download.html',locals())

def jupyter_views(request):
    PCILIST = Applist.objects.all()
    import socket
    ip = socket.gethostbyname(socket.gethostname())
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
    return render(request, 'process.html', locals())