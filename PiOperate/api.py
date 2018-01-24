import os
from django.http import HttpResponse
import json


def kill_process_api(request):
    try:
        pid = request.REQUEST['pid']
        os.system("kill -9 " + pid)
        ret = {'msg':'ok'}
    except:
        ret = {'msg':'fail'}
    return HttpResponse(json.dumps(ret))