import urllib.request
import time,re
import urllib,requests
from lxml import etree
from bs4 import BeautifulSoup

"""
重构v1.0版本
新增返回来源网站，跳转到短信的url
返回字段有区号列表：Area_code_list;手机号列表:phone_list;跳转到短信的url列表：country_url_list；来源网站：tempUrl
"""



def phon_data():
    url_list = ["http://www.z-sms.com/",  "https://yunduanxin.net/","https://www.we39.cn/"]
    #短信url合集"https://www.materialtools.com/",无+86号码http://www.114sim.com/，登录有人机交互 "https://www.bfkdim.com/home",
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]
    #print('开始检查：')
    for a in url_list:
        print(a)
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
            if len(phone):#http://www.z-sms.com/  跳转到短信的url
                # 存在值即为真
                print("存在数据")
                print("开始爬取数据http://www.z-sms.com/")
                country = "/lv.php?pho_num="
                country_url_list = []
                Area_code_list = []
                phone_list = []
                for i in Area:
                    # print(i.text)
                    Area_code_list.append(i.text)
                # print(area_list)
                for k in phone:
                    # print(i.text)
                    country_url=tempUrl+country
                    phone_list.append(k.text)
                    country_url_list.append(country_url)
                print(Area_code_list, phone_list, country_url_list, tempUrl)
                return Area_code_list, phone_list, country_url_list, tempUrl
            elif len(phone1):#https://yunduanxin.net/     跳转到短信urlh ttps://yunduanxin.net/info/8616574559124/
                print("存在数据")
                print("开始爬取数据https://yunduanxin.net/")
                country = "/info/"
                country_url_list = []
                Area_code_list = []
                phone_list = []
                for k in phone1:
                    # print(k.text)
                    qq = (k.text)
                    phone = qq.split(" ")  # 利用空格进行切割
                    #print(phone)
                    country_url=tempUrl+country
                    Area_code_list.append(phone[0])
                    phone_list.append(phone[1])
                    country_url_list.append(country_url)
                print(Area_code_list, phone_list, country_url_list, tempUrl)
                return Area_code_list, phone_list, country_url_list, tempUrl
            else:#https://www.we39.cn/  跳转到短信url   /receive/16533639083
                r = requests.get(tempUrl)
                htmls = r.text
                soup = BeautifulSoup(htmls, 'lxml')
                aaa = soup.find_all(class_=re.compile("card_num"))
                # print(aaa)
                country = "/receive/"
                country_url_list = []
                area_code = "+86"
                Area_code_list = []
                phone_lisr = []
                for aa in aaa:
                    bb = str(aa.text)
                    # print(aa.text)
                    pd_phone = re.compile(r'(?<=86)\d+\.?\d*')  # 以什么开头匹配
                    phone1 = pd_phone.findall(bb)
                    if len(phone1):  # 判断list为空
                        phone = "".join(phone1)  # 去掉list
                        # print(phone)
                        country_url = tempUrl+country
                        country_url_list.append(country_url)
                        Area_code_list.append(area_code)
                        phone_lisr.append(phone)
                print(Area_code_list, phone_list, country_url_list, tempUrl)
                return Area_code_list, phone_list, country_url_list, tempUrl
        except urllib.error.HTTPError:
            print(tempUrl + '=访问页面出错')
            time.sleep(2)
        except urllib.error.URLError:
            print(tempUrl + '=访问页面出错')
            time.sleep(2)
        time.sleep(0.1)

phon_data()