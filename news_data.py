import urllib.request
import time
import urllib,requests
from lxml import etree







url_list = ["http://www.z-sms.com/", "https://www.materialtools.com/", "https://yunduanxin.net/",
            "http://www.114sim.com/", "https://www.bfkdim.com/home",
            "https://www.we39.cn/"]#短信url合集
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
        phone = selector.xpath("//span[@class='btnCopy']")
        if len(phone):
            # 存在值即为真
            print("存在数据")
        else:
            # list_temp是空的
            print("不存在数据")

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
