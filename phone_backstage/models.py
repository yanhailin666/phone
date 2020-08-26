from django.db import models

# Create your models here.


class phone_test(models.Model):
    #id = models.CharField(max_length=30,verbose_name='id')
    phone = models.CharField(max_length=30,verbose_name='手机号')
    country = models.CharField(max_length=30,verbose_name='国家(默认为+86)')
    information_url = models.CharField(max_length=1000,verbose_name='跳转到短信url')
    source = models.CharField(max_length=100,verbose_name='来源网站')
    Creation_time = models.CharField(max_length=30,verbose_name='创建时间')

