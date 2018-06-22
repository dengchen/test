# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.test import TestCase

# Create your tests here.
from django.shortcuts import render,redirect,render_to_response,HttpResponse
import os, django,json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cscd.settings")
django.setup()
def main():
    list = [1,2,3]
    dict = {}
    dict['listData'] = list
    json1 = json.dumps(dict)

import json
def is_json(myjson):
 try:
    json_object = json.loads(myjson)
 except ValueError, e:
    return False
 return True

from cscdapp import models
def test():
    list1 = list(models.Company_nature.objects.all().values_list('Type'))
    print list1


print is_json('{"json_str": [1.2127500000000002, 1.05, 0, 0, 0.35, 0.35, 0.5543143749999999]}') #prints True

if __name__ == '__main__':
    test()