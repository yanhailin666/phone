from django.shortcuts import render
import urllib
from bs4 import BeautifulSoup
from .models import *
import json,requests
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.db import connection
import requests, json
import logging

logger = logging.getLogger("console")#配置日志

def analytic_coordinate(location_lat,location_lng):

    # location_lat="113.339929"#经度
    # location_lng="23.124703"#经度
    key="VLDBZ-YPTK6-R2GSK-MVXAM-746YJ-LCBBF"
    api_url="https://apis.map.qq.com/ws/geocoder/v1/?location="
    url=api_url+location_lng+","+location_lat+"&"+"key="+key+"&get_poi=1"
    #print(url)
    data=requests.get(url).text
    #print(data)
    analytic_data=json.loads(data)
    if str(analytic_data["status"])=="0":
        address=(analytic_data["result"]["address"])
        #print(address)
        return address
    elif str(analytic_data["status"])=="310":
        print("请求参数信息有误")
    elif str(analytic_data["status"])=="311":
        print("Key格式错误")
    elif str(analytic_data["status"])=="306":
        print("请求有护持信息请检查字符串")
    elif str(analytic_data["status"])=="110":
        print("请求来源未被授权")


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

def information(request,):#前端截取url进行跳转，暂时不用
    phone="13347470101"
    phone_dat = phone_test.objects.values().get(phone=phone)
    #print(goods["information_url"])
    url=phone_dat["information_url"]
    #url="http://m.baidu.com/"
    html=requests.get(url)
    return HttpResponse(html)

def add_gps_position(request):#get
    if request.method == 'GET':
        data=request.GET.get('data',"")
        print((data))
        title=request.GET.get('title')#标题
        content = request.GET.get('content')#内容`
        brand = request.GET.get('brand')#手机品牌
        model = request.GET.get('model')#手机型号
        time=str(request.GET.get('time'))#时间戳
        print(title,content,brand,model,time)
        model_data=gps_position.objects.create(title=title,content=content,phone_models=brand+";"+model+time)
        model_data.save()
    return JsonResponse({"data":"分享成功"})

def update_gps_position(request):
    if request.method == 'GET':
        data=request.GET.get('data',"")
        print((data))
    return JsonResponse({"data": "修改成功"})