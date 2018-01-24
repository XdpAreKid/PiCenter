#coding=utf-8
'''
# The modules contains PiApp's models 

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

from django.db import models
from django.contrib.auth.models import AbstractUser

import os

class Applist(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    url = models.URLField()
