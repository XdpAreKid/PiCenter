import os
from django.http import HttpResponse
import urllib.request, sys
import re
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

    info = os.popen('df -l').readlines()[1:]
    for i in info:
        result.append(i.split())

    return result


def get_system_uptime():
    time = os.popen('uptime').readlines()[0]
    result = time[time.find('up') + 3:].split(',  ')
    return result


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return (res.replace("temp=", "").replace("'C\n", ""))


# Return RAM information (unit=kb) in a list
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return (line.split()[1:4])


# Return % of CPU used by user as a character string

def getCPUuse():
    info = os.popen('ps aux').readlines()
    result = 0
    for line in info[1:]:
        get = line.split()
        result += float(get[2])
    return result


