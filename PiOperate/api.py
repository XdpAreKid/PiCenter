import os
from django.http import HttpResponse
import json
import socket
import fcntl
import struct
import platform

def get_ip_address(ifname='eth0'):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
      s.fileno(),
      0x8915, # SIOCGIFADDR
      struct.pack('256s', ifname[:15])
    )[20:24])
  except:
    ips = os.popen("LANG=C ifconfig | grep \"inet addr\" | grep -v \"127.0.0.1\" | awk -F \":\" '{print $2}' | awk '{print $1}'").readlines()
    if len(ips) > 0:
      return ips[0]
  return ''

def kill_process_api(request):
    try:
        pid = request.GET['pid']
        os.system("kill 9 " + pid)
        ret = {'msg':'ok'}
    except:
        ret = {'msg':'fail'}
    return HttpResponse(json.dumps(ret))

def get_release_info():
    return platform.uname()

def get_Filesystem_info():
    result = []

    info = os.popen('df -l').readlines()
    for i in info:
        result.append(i.split())

    return result

def get_cpu_temp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    temp = float(file.read()) / 1000
    file.close()
    return temp

def get_system_uptime():
    time = os.popen('uptime').readlines()[0]
    result = time[time.find('up') + 3:].split(',  ')
    return result