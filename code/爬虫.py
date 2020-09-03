import urllib.request
import pymysql, time
import requests
import re
from bs4 import BeautifulSoup
zrl="http://www.59xihuan.cn"
i=0
qburl=[]

def fxurl():#返回url
    for i in  range(1,2):
        i=str(i)
        ur="http://www.59xihuan.cn/meiwen/list_15_"
        l=".html"
        url=ur+i+l
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        #print(html)
        bs = BeautifulSoup(html, "html.parser")
        namelist1 = str(bs.findAll("h4"))
        #print(namelist1)
        pick = re.findall(r'<h4.+?href="(.+?)"', namelist1)#正则表达式
        #print(pick)
        for url2 in pick:
            wz=zrl+url2
            qburl.append(wz)
        #print(wburl)
        return qburl
fxurl()
for wburl in qburl:
    def pcbtnr_bt():#返回标题
        z=requests.get(wburl)
        z.encoding=z.apparent_encoding
        #print(z.encoding)
        soup=BeautifulSoup(z.text,features='html.parser')
        bt=soup.find('h4').text
        print(bt)
        nr=soup.find(class_="pic_text0").text
        #print(nr)
        #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return bt
    def pcbtnr_nr():#返回内容
        z=requests.get(wburl)
        z.encoding=z.apparent_encoding
        #print(z.encoding)
        soup=BeautifulSoup(z.text,features='html.parser')
        bt=soup.find('h4').text
        #print(bt)
        nr=soup.find(class_="pic_text0").text
        #print(nr)
        #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return nr

    # 连接数据库 mysql
    def connectDB():
        host = "127.0.0.1"
        dbName = "mood_cabin"
        user = "root"
        password = ""
        # 此处添加charset='utf8'是为了在数据库中显示中文，此编码必须与数据库的编码一致
        db = pymysql.connect(host, user, password, dbName, charset='utf8')
        return db
        cursorDB = db.cursor()
        return cursorDB

    def creatTable(createTableName):
        createTableSql = "CREATE TABLE IF NOT EXISTS " + createTableName + "(title VARCHAR(100),text  VARCHAR(1000000000),time VARCHAR(1000000000),clicks VARCHAR(10000))"
        DB_create = connectDB()
        cursor_create = DB_create.cursor()
        cursor_create.execute(createTableSql)
        DB_create.close()
        print('creat table ' + createTableName + ' successfully')
        return createTableName

    def inserttable(insertTable,insertTitle, insertText, insertTime, insertClicks):
        insertContentSql = "INSERT INTO " + insertTable + "(title,content,create_date,create_by)VALUES(%s,%s,%s,%s)"
        #         insertContentSql="INSERT INTO "+insertTable+"(title,text,time,clicks)VALUES("+insertTitle+" , "+insertText+" ,"+insertTime+" ,  "+insertClicks+")"

        DB_insert = connectDB()
        cursor_insert = DB_insert.cursor()
        cursor_insert.execute(insertContentSql, (insertTitle, insertText, insertTime, insertClicks))
        DB_insert.commit()
        DB_insert.close()
        #print('inert contents to  ' + insertTable + ' successfully')

    def time_sj():
        a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        #print(a)
        return a




# #creatTable("wenben")
# time_sj()
    inserttable("mood_cabin_mood",pcbtnr_bt(),pcbtnr_nr(),time_sj(),"yhl")
#
#
#
#
#



















# import urllib.request
# import pymysql, time
# import requests
# import re
# from bs4 import BeautifulSoup
# zrl="http://www.59xihuan.cn"
# i=0
# qburl=[]
#
# def fxurl():#返回url
#     for i in  range(1,2):
#         i=str(i)
#         ur="http://www.59xihuan.cn/meiwen/list_15_"
#         l=".html"
#         url=ur+i+l
#         page = urllib.request.urlopen(url)
#         html = page.read().decode('utf-8')
#         #print(html)
#         bs = BeautifulSoup(html, "html.parser")
#         namelist1 = str(bs.findAll("h4"))
#         #print(namelist1)
#         pick = re.findall(r'<h4.+?href="(.+?)"', namelist1)#正则表达式
#         #print(pick)
#         for url2 in pick:
#             wz=zrl+url2
#             qburl.append(wz)
#         #print(wburl)
#         return qburl
# fxurl()
# for wburl in qburl:
#     def pcbtnr_bt():#返回标题
#         z=requests.get(wburl)
#         z.encoding=z.apparent_encoding
#         #print(z.encoding)
#         soup=BeautifulSoup(z.text,features='html.parser')
#         bt=soup.find('h4').text
#         print(bt)
#         nr=soup.find(class_="pic_text0").text
#         #print(nr)
#         #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#         return bt
#     def pcbtnr_nr():#返回内容
#         z=requests.get(wburl)
#         z.encoding=z.apparent_encoding
#         #print(z.encoding)
#         soup=BeautifulSoup(z.text,features='html.parser')
#         bt=soup.find('h4').text
#         #print(bt)
#         nr=soup.find(class_="pic_text0").text
#         #print(nr)
#         #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#         return nr
#
#     # 连接数据库 mysql
#     def connectDB():
#         host = "127.0.0.1"
#         dbName = "test"
#         user = "root"
#         password = ""
#         # 此处添加charset='utf8'是为了在数据库中显示中文，此编码必须与数据库的编码一致
#         db = pymysql.connect(host, user, password, dbName, charset='utf8')
#         return db
#         cursorDB = db.cursor()
#         return cursorDB
#
#     def creatTable(createTableName):
#         createTableSql = "CREATE TABLE IF NOT EXISTS " + createTableName + "(title VARCHAR(100),text  VARCHAR(1000000000),time VARCHAR(1000000000),clicks VARCHAR(10000))"
#         DB_create = connectDB()
#         cursor_create = DB_create.cursor()
#         cursor_create.execute(createTableSql)
#         DB_create.close()
#         print('creat table ' + createTableName + ' successfully')
#         return createTableName
#
#     def inserttable(insertTable, insertTitle, insertText, insertTime, insertClicks):
#         insertContentSql = "INSERT INTO " + insertTable + "(title,text,time,clicks)VALUES(%s,%s,%s,%s)"
#         #         insertContentSql="INSERT INTO "+insertTable+"(title,text,time,clicks)VALUES("+insertTitle+" , "+insertText+" ,"+insertTime+" ,  "+insertClicks+")"
#
#         DB_insert = connectDB()
#         cursor_insert = DB_insert.cursor()
#         cursor_insert.execute(insertContentSql, (insertTitle, insertText, insertTime, insertClicks))
#         DB_insert.commit()
#         DB_insert.close()
#         print('inert contents to  ' + insertTable + ' successfully')
#
#     def time_sj():
#         a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#         return a
#
#
#
#
# # #creatTable("wenben")
# # time_sj()
#     inserttable("wenben",pcbtnr_bt(),pcbtnr_nr(),time_sj(),"yhl")
# #
# #
# #
# #
# #
#
#
#
#
#
#
