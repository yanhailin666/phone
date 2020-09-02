import requests,re
from bs4 import BeautifulSoup





url = "https://www.we39.cn/"
r = requests.get(url)
htmls = r.text
soup = BeautifulSoup(htmls, 'lxml')
aaa=soup.find_all(class_=re.compile("card_num"))
#print(aaa)
country_url="/receive/"
country_url_list = []
area_code="+86"
area_code_list=[]
phone_lisr = []
for aa in aaa:
    bb=str(aa.text)
    #print(aa.text)
    pd_phone=re.compile(r'(?<=86)\d+\.?\d*')#以什么开头匹配
    phone1=pd_phone.findall(bb)
    if len(phone1):#判断list为空
        phone="".join(phone1)#去掉list
        #print(phone)
        dx_url=country_url+phone
        country_url_list.append(dx_url)
        area_code_list.append(area_code)
        phone_lisr.append(phone)
print(country_url_list,area_code_list,phone_lisr,)
