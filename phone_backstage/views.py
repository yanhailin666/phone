from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import urllib
from bs4 import BeautifulSoup
from .models import *

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
