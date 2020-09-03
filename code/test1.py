import requests,re
from bs4 import BeautifulSoup
url = "https://www.we39.cn/"
r = requests.get(url)
htmls = r.text
#print(htmls)
#soup = BeautifulSoup(htmls, 'html.parser')
# soup = BeautifulSoup("<span></span>", "html.parser")
# # # # # # 只有起始标签的会自动补全，只有结束标签的灰自动忽略
# # # # # # 结果为：<a></a>
# # # # # soup = BeautifulSoup("<a></p>", "lxml")
# # # # # #结果为：<html><body><a></a></body></html>
# # # # # soup = BeautifulSoup("<a></p>", "html5lib")
# # # # # # html5lib则出现一般的标签都会自动补全
# # # # # # 结果为：<html><head></head><body><a><p></p></a></body></html>

# html = '<p class="title" id="p1"><b>The Dormouses story</b></p>'
soup = BeautifulSoup(htmls, 'lxml')
#根据class的名称获取p标签内的所有内容
# soup.find(class_="card_num")
#或者
# soup.find("p",class_="title" id = "p1")
# #获取class为title的p标签的文本内容"The Dormouse's story"
# aa=soup.find(class_="card_num").get_text()
# print(aa)
# #获取文本内容时可以指定不同标签之间的分隔符，也可以选择是否去掉前后的空白。
# soup = BeautifulSoup('<p class="title" id="p1"><b> The Dormouses story </b></p><p class="title" id="p1"><b>The Dormouses story</b></p>', "html5lib")
# soup.find(class_="title").get_text("|", strip=True)
# #结果为：The Dormouses story|The Dormouses story
# #获取class为title的p标签的id
# soup.find(class_="title").get("id")
# #对class名称正则：
aaa=soup.find_all(class_=re.compile("card_num"))
#print(aaa)

for aa in aaa:
    bb=str(aa.text)
    #print(aa.text)
    cc=re.compile(r'(?<=86)\d+\.?\d*')#以什么开头匹配
    xx=cc.findall(bb)
    print(xx)

# #recursive参数，recursive=False时，只find当前标签的第一级子标签的数据
# soup = BeautifulSoup('<html><head><title>abc','lxml')
# aa=soup.html.find_all("card_num", recursive=False)
# print(aa)