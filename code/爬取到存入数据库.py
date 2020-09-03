import urllib.request
import pymysql, time
import requests
import re
from bs4 import BeautifulSoup
zrl="http://www.59xihuan.cn"
i=0

def fxurl():
    for i in  range(1,2):
        i=str(i)
        ur="http://www.59xihuan.cn/meiwen/list_15_"
        l=".html"
        url=ur+i+l
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        #print(html)
        return html
def pcbtnr_bt():
    html = fxurl()
    bs = BeautifulSoup(html, "html.parser")
    namelist = bs.findAll("h4")
    #print(namelist)
    for i in namelist:
        #print(i)
        i=str(i)
        a=i.split('"')
        #a=(''.join(i))
        #print(a)
        #print(a[1])
        lj=a[1]
        ll=lj[0:7]
        #print(ll)
        if ll =="/meiwen":
            url1=zrl+lj
            #print(url1)
            z=requests.get(url1)
            z.encoding=z.apparent_encoding
            #print(z.encoding)
            soup=BeautifulSoup(z.text,features='html.parser')
            bt=soup.find('h4').text
            print(bt)
            nr=soup.find(class_="pic_text0").text
            #print(nr)
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return bt
def pcbtnr_nr():
    html = fxurl()
    bs = BeautifulSoup(html, "html.parser")
    namelist = bs.findAll("h4")
    #print(namelist)
    for i in namelist:
        #print(i)
        i=str(i)
        a=i.split('"')
        #a=(''.join(i))
        #print(a)
        #print(a[1])
        lj=a[1]
        ll=lj[0:7]
        #print(ll)
        if ll =="/meiwen":
            url1=zrl+lj
            #print(url1)
            z=requests.get(url1)
            z.encoding=z.apparent_encoding
            #print(z.encoding)
            soup=BeautifulSoup(z.text,features='html.parser')
            bt=soup.find('h4').text
            #print(bt)
            nr=soup.find(class_="pic_text0").text
            print(nr)
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            return nr

# 连接数据库 mysql
def connectDB():
    host = "127.0.0.1"
    dbName = "test"
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

def inserttable(insertTable, insertTitle, insertText, insertTime, insertClicks):
    insertContentSql = "INSERT INTO " + insertTable + "(title,text,time,clicks)VALUES(%s,%s,%s,%s)"
    #         insertContentSql="INSERT INTO "+insertTable+"(title,text,time,clicks)VALUES("+insertTitle+" , "+insertText+" ,"+insertTime+" ,  "+insertClicks+")"

    DB_insert = connectDB()
    cursor_insert = DB_insert.cursor()
    cursor_insert.execute(insertContentSql, (insertTitle, insertText, insertTime, insertClicks))
    DB_insert.commit()
    DB_insert.close()
    print('inert contents to  ' + insertTable + ' successfully')

def time_sj():
    a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return a



fxurl()
pcbtnr_bt()
pcbtnr_nr()
connectDB()
time_sj()
inserttable("test",pcbtnr_bt(),pcbtnr_nr(),time_sj(),"yhl")







