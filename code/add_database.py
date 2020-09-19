import pymysql,time
from phone_data import sms
from phone_data import yunduanxin


#实例化爬取数据函数
sms_data=sms()
yunduanxin_data=yunduanxin()
#两个list合并一个list
print(sms_data)
print(yunduanxin_data)
phone_list=sms_data[1]+yunduanxin_data[1]
Area_code_list=sms_data[0]+yunduanxin_data[0]
country_url_list=sms_data[2]+yunduanxin_data[2]
source_list=sms_data[3]+yunduanxin_data[3]

for phone,Area_code,country_url,source in zip(phone_list,Area_code_list,country_url_list,source_list):
    print(phone,Area_code,country_url)
    def connectDB():
        host = "127.0.0.1"#数据库地址
        dbName = "test"#数据库名
        user = "root"#表名
        password = ""#密码
        # 此处添加charset='utf8'是为了在数据库中显示中文，此编码必须与数据库的编码一致
        db = pymysql.connect(host, user, password, dbName, charset='utf8')
        return db
        cursorDB = db.cursor()
        return cursorDB


    # def creatTable(createTableName):
    # #     createTableSql = "CREATE TABLE IF NOT EXISTS " + createTableName + "(title VARCHAR(100),text  VARCHAR(1000000000),time VARCHAR(1000000000),clicks VARCHAR(10000))"
    # #     DB_create = connectDB()
    # #     cursor_create = DB_create.cursor()
    # #     cursor_create.execute(createTableSql)
    # #     DB_create.close()
    # #     print('creat table ' + createTableName + ' successfully')
    # #     return createTableName


    def inserttable(insertTable, insertPhone, insertcountry, insertinformation_url, insertsource,insertCreation_time):
        insertContentSql = "INSERT INTO " + insertTable + "(phone,country,information_url,source,Creation_time)VALUES(%s,%s,%s,%s,%s)"
        #         insertContentSql="INSERT INTO "+insertTable+"(title,text,time,clicks)VALUES("+insertTitle+" , "+insertText+" ,"+insertTime+" ,  "+insertClicks+")"

        DB_insert = connectDB()
        cursor_insert = DB_insert.cursor()
        cursor_insert.execute(insertContentSql, (insertPhone, insertcountry, insertinformation_url, insertsource,insertCreation_time))
        DB_insert.commit()
        DB_insert.close()
        # print('inert contents to  ' + insertTable + ' successfully')


    def time_sj():
        a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # print(a)
        return a

    inserttable("phone_backstage_phone_test",phone,Area_code,country_url,source,time_sj())