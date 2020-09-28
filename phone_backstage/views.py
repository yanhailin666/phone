from django.shortcuts import render
import urllib
from bs4 import BeautifulSoup
from .models import *
import json,requests
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.db import connection

import logging
logger = logging.getLogger("console")#配置日志


def china(request):
    json_list = []
    goods = phone_test.objects.all()
    for good in goods:
        json_dict = {}
        aa = good.country
        bb =good.information_url
        if aa.rstrip() == "+86":
            json_dict["country"] = good.country
            json_dict["information_url"] = good.information_url
            if bb =="https://yunduanxin.net/info/":
                json_dict["phone"] = "86"+good.phone
            else:
                json_dict["phone"] = good.phone
            json_list.append(json_dict)
        else:
            pass
    return JsonResponse({"json_list": json_list})


def overseas(request):
    json_list = []
    goods = phone_test.objects.all()
    for good in goods:
        json_dict = {}
        aa = good.country
        if aa.rstrip() == "+86":
            pass
        else:
            json_dict["country"] = good.country
            json_dict["phone"] = good.phone
            json_dict["information_url"] = good.information_url
            json_list.append(json_dict)
    return JsonResponse({"json_list": json_list})

def information(request,):
    phone="13347470101"
    phone_dat = phone_test.objects.values().get(phone=phone)
    #print(goods["information_url"])
    url=phone_dat["information_url"]
    #url="http://m.baidu.com/"
    html=requests.get(url)
    return HttpResponse(html)
