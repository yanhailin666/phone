from selenium import webdriver
import os, time

# 加载启动项
option = webdriver.ChromeOptions()
option.add_argument('headless')

# 定义截图地址&图片格式
screen_path = os.path.dirname(os.getcwd()) + '/report/Screenshots/'
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
screen_name = screen_path + rq + '.png'

# 打开chrome浏览器

# driver = webdriver.Chrome(chrome_options=option)

# 版本更新，需要options 代替chrome_option
driver = webdriver.Chrome(options=option)

# 定义url 地址
url = 'http://www.baidu.com'

driver.get(url=url)
time.sleep(2)

# 截图
driver.save_screenshot(screen_name)
time.sleep(3)

# 退出并关闭浏览器
driver.quit()














# from selenium.common.exceptions import NoSuchElementException#判断元素是否存在
# from selenium.common.exceptions import NoAlertPresentException
# import urllib,requests
# from lxml import etree
# from bs4 import BeautifulSoup
#
#
#
#
# url = "https://www.baidu.com"
# page = urllib.request.urlopen(url)
# html = page.read().decode('utf-8')
# selector = etree.HTML(html)
# z=requests.get(url)
# z.encoding=z.apparent_encoding
# #print(z.encoding)
# soup=BeautifulSoup(z.text,features='html.parser')
# bt=soup.find('div').text
# print(bt)
# try:
#     nr=soup.find(class_="pic_text0")
#     print(nr)
# except NoSuchElementException:
#     print("元素不存在")
# Area = selector.xpath("//a[@class='c-color-gray2']")
# print(Area)
# # aa=selector.
# #
# #
# #
# #
# # try:
# #
# # except NoSuchElementException:#判断元素是否存在
# #     print("元素不存在")
