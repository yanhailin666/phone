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

#selenium判断元素为空时
"""
from selenium.common.exceptions import NoSuchElementException#判断元素是否存在
from selenium.common.exceptions import NoAlertPresentException
try:
    nr=soup.find(class_="pic_text0")
    print(nr)
except NoSuchElementException:
    print("元素不存在")
"""

#判断list为空时
"""
if len(phone):
    # 存在值即为真
    print("存在数据")
else:
    # list_temp是空的
    print("不存在数据")

"""

