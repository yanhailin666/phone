import urllib,requests
from lxml import etree
from bs4 import BeautifulSoup
import re





url = "https://www.we39.cn/"
page = urllib.request.urlopen(url)
html = page.read().decode('utf-8')
#print(html)
bs = BeautifulSoup(html, "html.parser")
namelist1 = str(bs.findAll("span"))#选取标签为span
#print(namelist1)
Area_url_list= re.findall(r'<span.+?href="(.+?)"', namelist1)
#print(pick)
country_url_list=[]
phone_lisr=[]
for Area_url in Area_url_list:
    #print(i)
    phone=Area_url.split("/")
    #print(aa)
    country_url_list.append(Area_url)
    phone_lisr.append(phone[2])
print(country_url_list,phone_lisr)



































# page = urllib.request.urlopen(url)
# html = page.read().decode('utf-8')
# #print(html)
# selector = str(etree.HTML(html))
# #print(selector.text)
# # 转化成矿业识别的xpath
# #phone = selector.xpath("//span[@class='card_read btnCopy']/[@data-clipboard-text]")
# MOBILE = "^1[358]\d{9}$|^147\d{8}$|^179\d{8}$"
# phone = re.compile(MOBILE)
# #print(phone)
# if phone.match(selector):
#     print(selector)
# # if len(phone):
# #     # 存在值即为真
# #     print("存在数据")
# #     country_list = []
# #     phone_list = []
# #     for k in phone:
# #         print(k.text)
# #     #     aa=(k.text)
# #     #     bb=aa.split(" ")#利用空格进行切割
# #     #     #print(bb)
# #     #     country_list.append(bb[0])
# #     #     phone_list.append(bb[1])
# #     # print(country_list,phone_list)
# #
# # else:
# #     # list_temp是空的
# #     print("不存在数据")
# #
# #
# #
