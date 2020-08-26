import urllib.request
import time
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]
# 这个是你放网址的文件名，改过来就可以了
aa=["http://127.0.0.1:8000/","https://www.baidu.com","http://127.0.0.1:8000/","http://127.0.1.1:8000/","http://127.0.0.1:8000/admin"]
print('开始检查：')
for a in aa:
    tempUrl = a
    try:
        opener.open(tempUrl)
        print(tempUrl + '没问题')
    except urllib.error.HTTPError:
        print(tempUrl + '=访问页面出错')
        time.sleep(2)
    except urllib.error.URLError:
        print(tempUrl + '=访问页面出错')
        time.sleep(2)
    time.sleep(0.1)
