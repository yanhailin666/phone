import urllib.request
import time,re
import urllib,requests
from lxml import etree
from bs4 import BeautifulSoup

"""
这个爬虫的代码需要重构
问题1.不是所有的跳转到短信的链接都有规律，有部分有号码，有部分没有号码。需要存跳转到短信的url
问题2.有一些网站做了人机交互，需要破解
"""





url_list = ["http://www.z-sms.com/",  "https://yunduanxin.net/","https://www.we39.cn/"]
#短信url合集"https://www.materialtools.com/",无+86号码http://www.114sim.com/，登录有人机交互 "https://www.bfkdim.com/home",
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]

print('开始检查：')
for a in url_list:
    tempUrl = a
    try:#判断url是否可以打开
        opener.open(tempUrl)
        print(tempUrl + '没问题')
        page = urllib.request.urlopen(tempUrl)
        html = page.read().decode('utf-8')
        # print(html)
        selector = etree.HTML(html)  # 转化成矿业识别的xpath,这边转化成一个列表，对文字没有作用
        # =selector.xpath("//p[@class='number']|//span[@class='btnCopy']")# 选取所有的class属性"|"这个为多个路径
        # print(phone)
        Area = selector.xpath("//p[@class='number']")#利用xpath定位获取数据
        phone = selector.xpath("//span[@class='btnCopy']")#http://www.z-sms.com/
        phone1 = selector.xpath("//h4[@class='number-boxes-item-number']")#https://yunduanxin.net/
        if len(phone):
            # 存在值即为真
            print("存在数据")
            print("开始爬取数据")
            country_list = []
            phone_list = []
            for i in Area:
                # print(i.text)
                country_list.append(i.text)
            # print(area_list)
            for k in phone:
                # print(i.text)
                phone_list.append(k.text)
            # print(phone_list)
            # a_tuple = tuple(phone_list)#list转元祖
            # print(a_tuple)
            # daat_dict = dict(zip(area_list, phone_list))
            # print(daat_dict)
            # country_list = daat_dict.keys()
            # phone_list = daat_dict.values()
            #return country_list, phone_list, tempUrl
        elif len(phone1):#https://yunduanxin.net/     跳转到短信urlh ttps://yunduanxin.net/info/8616574559124/
            print("存在数据")
            print("开始爬取数据")
            country_list = []
            phone_list = []
            for k in phone:
                # print(k.text)
                aa = (k.text)
                bb = aa.split(" ")  # 利用空格进行切割
                # print(bb)
                country_list.append(bb[0])
                phone_list.append(bb[1])
            print(country_list, phone_list)
            # return country_list, phone_list, tempUrl
        else:#https://www.we39.cn/
            page = urllib.request.urlopen(tempUrl)
            html = page.read().decode('utf-8')
            # print(html)
            bs = BeautifulSoup(html, "html.parser")
            namelist1 = str(bs.findAll("span"))  # 选取标签为span
            # print(namelist1)
            Area_url_list = re.findall(r'<span.+?href="(.+?)"', namelist1)
            # print(pick)
            country_url_list = []
            Area_code_list=[]
            phone_lisr = []
            for Area_url in Area_url_list:
                # print(i)
                phone = Area_url.split("/")
                # print(aa)
                country_url_list.append(Area_url)
                phone_lisr.append(phone[2])
            #print(country_url_list, phone_lisr)
            # return country_list, phone_list, tempUrl

            # # list_temp是空的
            # print("不存在数据")

        # area_list = []
        # phone_list = []
        # for i in Area:
        #     # print(i.text)
        #     area_list.append(i.text)
        # # print(area_list)
        # for k in phone:
        #     # print(i.text)
        #     phone_list.append(k.text)
        # # print(phone_list)
        # # a_tuple = tuple(phone_list)#list转元祖
        # # print(a_tuple)
        # daat_dict = dict(zip(area_list, phone_list))
        # print(daat_dict)
        # country_list = daat_dict.keys()
        # phone_list = daat_dict.values()
        # return country_list, phone_list, tempUrl
    except urllib.error.HTTPError:
        print(tempUrl + '=访问页面出错')
        time.sleep(2)
    except urllib.error.URLError:
        print(tempUrl + '=访问页面出错')
        time.sleep(2)
    time.sleep(0.1)
