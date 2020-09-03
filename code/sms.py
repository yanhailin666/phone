import urllib,requests
from lxml import etree


def phone_data():
    url="http://www.z-sms.com/"
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    #print(html)
    selector=etree.HTML(html)#转化成矿业识别的xpath,这边转化成一个列表，对文字没有作用
    #=selector.xpath("//p[@class='number']|//span[@class='btnCopy']")# 选取所有的class属性"|"这个为多个路径
    #print(phone)
    Area=selector.xpath("//p[@class='number']")
    phone=selector.xpath("//span[@class='btnCopy']")
    area_list=[]
    phone_list=[]
    for i in Area:
        #print(i.text)
        area_list.append(i.text)
    #print(area_list)
    for k in phone:
        #print(i.text)
        phone_list.append(k.text)
    #print(phone_list)
    # a_tuple = tuple(phone_list)#list转元祖
    # print(a_tuple)
    daat_dict=dict(zip(area_list,phone_list))
    print(daat_dict)
    country_list = daat_dict.keys()
    phone_list = daat_dict.values()
    return country_list,phone_list,url




def phone_data1():
    url="http://www.xnsms.com/"
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    #print(html)
    selector=etree.HTML(html)#转化成矿业识别的xpath
    #=selector.xpath("//p[@class='number']|//span[@class='btnCopy']")# 选取所有的class属性"|"这个为多个路径
    #print(phone)
    Area=selector.xpath("//p[@class='number']")
    phone=selector.xpath("//span[@class='btnCopy']")
    area_list=[]
    phone_list=[]
    for i in Area:
        #print(i.text)
        area_list.append(i.text)
    print(area_list)
    for k in phone:
        #print(i.text)
        phone_list.append(k.text)
    print(phone_list)
    # a_tuple = tuple(phone_list)#list转元祖
    # print(a_tuple)
phone_data()
#phone_data1()