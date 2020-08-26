from django.http import HttpResponse
import urllib
from bs4 import BeautifulSoup

import logging
logger = logging.getLogger("console")#配置日志


def home(request):
    
    return HttpResponse()



def information(request):
    url = 'http://www.z-sms.com/lv.php?pho_num=17194242613&1'
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    # print(html)
    bs = BeautifulSoup(html, "html.parser")
    nr = bs.find(class_="container")
    print(nr)
    return HttpResponse(html)


