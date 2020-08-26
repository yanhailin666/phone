import urllib,requests
from lxml import etree
from bs4 import BeautifulSoup





url = "https://baike.baidu.com/item/1111%E5%B9%B4/5231482?fr=aladdin"
page = urllib.request.urlopen(url)
html = page.read().decode('utf-8')
# print(html)
selector = etree.HTML(html)  # 转化成矿业识别的xpath
# =selector.xpath("//p[@class='number']|//span[@class='btnCopy']")# 选取所有的class属性"|"这个为多个路径
# print(phone)
#Area = selector.xpath("//p[@class='number']")

phone = selector.xpath("//div[@class='para']")
print(phone)
if len(phone):
    # 存在值即为真
    print("存在数据")
else:
    # list_temp是空的
    print("不存在数据")



