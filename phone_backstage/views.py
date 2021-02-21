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

def analytic_coordinate(request):
    location_lat = "113.419324"  # 经度
    location_lng = "23.158925"  # 纬度
    key="VLDBZ-YPTK6-R2GSK-MVXAM-746YJ-LCBBF"
    api_url="https://apis.map.qq.com/ws/geocoder/v1/?location="
    url=api_url+location_lng+","+location_lat+"&"+"key="+key+"&get_poi=1"
    #print(url)
    data=requests.get(url).text
    #print(data)
    analytic_data=json.loads(data)
    if str(analytic_data["status"])=="0":
        address=(analytic_data["result"]["address"])
        print(address)
    elif str(analytic_data["status"])=="310":
        print ("请求参数信息有误")
    elif str(analytic_data["status"])=="311":
        print ("Key格式错误")
    elif str(analytic_data["status"])=="306":
        print ("请求有护持信息请检查字符串")
    elif str(analytic_data["status"])=="110":
        print ("请求来源未被授权")
    return JsonResponse({"data": "修改成功"})


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
        #print((data))
        title=request.GET.get('title')#标题
        content = request.GET.get('content')#内容`
        brand = request.GET.get('brand')#手机品牌
        model = request.GET.get('model')#手机型号
        time= request.GET.get('time')#时间戳
        #print(title,content,brand,model,time)
        phone_models=str(brand)+";"+str(model)
        model_data=gps_position.objects.create(title=title,content=content,phone_models=phone_models,time=time)
        model_data.save()
    return JsonResponse({"data":"分享成功"})

def update_gps_position(request):
    if request.method == 'GET':
        data=request.GET.get('data',"")
        #print((data))
        time = request.GET.get('time')  # 时间戳
        lng= str(request.GET.get('lng'))#经度
        lat= str(request.GET.get('lat'))#纬度
        crea_time=int(request.GET.get('creatime'))#保存时间戳
        time_local = time.localtime(crea_time / 1000)#需要转换时间戳
        creation_time= time.strftime("%Y-%m-%d %H:%M:%S", time_local)#输出时间格式
        key = "VLDBZ-YPTK6-R2GSK-MVXAM-746YJ-LCBBF"
        api_url = "https://apis.map.qq.com/ws/geocoder/v1/?location="
        #url = api_url + lng + "," + lat + "&" + "key=" + key + "&get_poi=1"
        url = api_url + lat + "," + lng + "&" + "key=" + key + "&get_poi=1"
        print(url)
        data = requests.get(url).text
        # print(data)
        analytic_data = json.loads(data)
        if str(analytic_data["status"]) == "0":
            address = (analytic_data["result"]["address"])
            # print(address)
            query_databates = gps_position.objects.get(time=time)  # 查询time时间戳为一样的进行修改
            query_databates.latitude = lat
            query_databates.longitude = lng
            query_databates.detailed_address = address
            query_databates.creation_time=creation_time
            query_databates.save()  # 执行更新数据库
        elif str(analytic_data["status"]) == "310":
            print("请求参数信息有误")
        elif str(analytic_data["status"]) == "311":
            print("Key格式错误")
        elif str(analytic_data["status"]) == "306":
            print("请求有护持信息请检查字符串")
        elif str(analytic_data["status"]) == "110":
            print("请求来源未被授权")
        # /phone/update_gps_position?lng=113.419324&lat=23.158925&time=&title=%E6%B8%A9%E6%9F%94&content=%E7%8B%97%E7%8D%BE
    return JsonResponse({"data": "修改成功"})

def query_gps_position(request):#查询地址
    if request.method == 'GET':
        data=request.GET.get('data',"")
        #print((data))
        brand = request.GET.get('brand')#手机品牌
        model = request.GET.get('model')#手机型号
        phone_models = str(brand) + ";" + str(model)
        #print(phone_models)
        query_databates=gps_position.objects.filter(phone_models=phone_models)#按手机型号进行查询
        #print(query_databates)
        address_list=[]
        for address in query_databates:#获取地址信息
            address_dict={}
            address_dict["id"]=address.id#数据库id
            address_dict["address"]=address.detailed_address#地址信息
            address_dict["lat"]=address.latitude#纬度
            address_dict["lng"]=address.longitude#经度
            address_dict["change_time"]=address.creation_time#保存时间
            address_list.append(address_dict)
        #print(address_list)
        return JsonResponse({"address_list":address_list})#返回地址到前端
        #return JsonResponse({"data": "查询成功"})