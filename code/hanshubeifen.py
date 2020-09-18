from django.shortcuts import render
import urllib
from bs4 import BeautifulSoup
from .models import *
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

import logging
logger = logging.getLogger("console")#配置日志


def china(request):
    id = request.GET.get('id')
    dict = phone_test.objects.values().all()
    #print(dict)
    country_list = []
    phone_list = []
    information_list = []
    for data in dict:
        # print(type(data["country"]))
        if data["country"].rstrip() == "+86":  # a.rstrip()去掉结尾的空格
            country_list.append(data["country"])
            phone_list.append(data["phone"])
            information_list.append(data["information_url"])
        else:
            pass
    return JsonResponse({"country_list": country_list, "phone_list": phone_list, 'information_list': information_list})


def overseas(request):
    id = request.GET.get('id')
    dict = phone_test.objects.values().all()
    #print(dict)
    country_list=[]
    phone_list=[]
    information_list=[]
    for data in dict:
        #print(type(data["country"]))
        if data["country"].rstrip()=="+86":#a.rstrip()去掉结尾的空格
            pass
        else:
            country_list.append(data["country"])
            phone_list.append(data["phone"])
            information_list.append(data["information_url"])
    return JsonResponse({"country_list": country_list, "phone_list": phone_list, 'information_list': information_list})

def information(request):
    url = 'http://www.z-sms.com/lv.php?pho_num=17194242613&1'
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    # print(html)
    bs = BeautifulSoup(html, "html.parser")
    nr = bs.find(class_="container")
    #print(nr)
    return HttpResponse(html)


def test(request):
    json_list = []
    goods = phone_test.objects.all()
    for good in goods:
        json_dict = {}
        aa=good.country
        if aa.rstrip()=="+86":
            json_dict["country"] = good.country
            json_dict["phone"] = good.phone
            json_dict["information_url"] = good.information_url
            json_list.append(json_dict)
    return JsonResponse({"json_list":json_list})

# def aa(request):
#     with connection.cursor() as cursor:
#         cursor.execute('select id, machine, tomcathome, ipaddress, description from tomcatData')
#         data = dictfetchall(cursor)
#     return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
#     # # 使用ORM
#     # # all()返回的是QuerySet 数据类型；values()返回的是ValuesQuerySet 数据类型
#     #
#     # data = phone_test.VM.objects.values('id', 'country', 'phone', 'information_url')
#     #
#     # data = serializers.serialize("json", data)
#     #
#     # return JsonResponse(list(data), safe=False)
