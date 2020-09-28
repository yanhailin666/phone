import urllib.request
import time,re
import urllib,requests
from lxml import etree
from bs4 import BeautifulSoup

"""
重构v2.0版本 
每一个网站写一个函数
"""


def sms():#http://www.z-sms.com
    url='http://www.z-sms.com'
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0')]
    #print('开始检查：')
    tempUrl =url
    try:#判断url是否可以打开
        opener.open(tempUrl)
        print(tempUrl + '没问题')
        page =requests.get(url).text
        #print(page)
        selector = etree.HTML(page)  # 转化成矿业识别的xpath,这边转化成一个列表，对文字没有作用
        Area = selector.xpath("//p[@class='number']")#利用xpath定位获取数据
        phone = selector.xpath("//span[@class='btnCopy']")#http://www.z-sms.com
        if len(Area):#http://www.z-sms.com/  跳转到短信的url
            # 存在值即为真
            print("存在数据")
            print("开始爬取数据http://www.z-sms.com/")
            country = "/lv.php?pho_num="
            country_url_list = []
            Area_code_list = []
            phone_list = []
            tempUrl_list=[]
            for i in Area:
                # print(i.text)
                Area_code_list.append(i.text)
            # print(area_list)
            for k in phone:
                # print(i.text)
                country_url=tempUrl+country+k.text
                phone_list.append(k.text)
                country_url_list.append(country_url)
                tempUrl_list.append(tempUrl)
            #print(Area_code_list, phone_list, country_url_list, tempUrl_list)
            return Area_code_list, phone_list, country_url_list, tempUrl_list
        else:
            pass
    except urllib.error.HTTPError:
        print(tempUrl + '=访问页面出错')
        time.sleep(2)
    except urllib.error.URLError:
        print(tempUrl + '=访问页面出错')
        time.sleep(2)


def yunduanxin():
    url= "https://yunduanxin.net"
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]
    # print('开始检查：')
    tempUrl = url
    try:  # 判断url是否可以打开
        opener.open(tempUrl)
        print(tempUrl + '没问题')
        page = urllib.request.urlopen(tempUrl)
        html = page.read().decode('utf-8')
        # print(html)
        selector = etree.HTML(html)  # 转化成矿业识别的xpath,这边转化成一个列表，对文字没有作用
        phone1 = selector.xpath("//h4[@class='number-boxes-item-number']")  # https://yunduanxin.net/
        if len(phone1):
            print("存在数据")
            print("开始爬取数据https://yunduanxin.net/")
            country = "/info/"
            country_url_list = []
            Area_code_list = []
            phone_list = []
            tempUrl_list = []
            for k in phone1:
                # print(k.text)
                qq = (k.text)
                phone = qq.split(" ")  # 利用空格进行切割
                #print(phone[0])
                Area_code_code= re.findall("\d+", phone[0])#匹配数字
                #print(Area_code_code)
                for match in Area_code_code:
                    pass
                    #print(match)
                country_url = tempUrl + country+match+phone[1]+"/"
                #print(country_url)
                Area_code_list.append(phone[0])
                phone_list.append(phone[1])
                country_url_list.append(country_url)
                tempUrl_list.append(tempUrl)
            #print(Area_code_list, phone_list, country_url_list, tempUrl_list)
            return Area_code_list, phone_list, country_url_list, tempUrl_list
        else:  # https://www.we39.cn/  跳转到短信url   /receive/16533639083
            pass
    except urllib.error.HTTPError:
        print(tempUrl + '=访问页面出错')
        time.sleep(2)
    except urllib.error.URLError:
        print(tempUrl + '=访问页面出错')
        time.sleep(2)

