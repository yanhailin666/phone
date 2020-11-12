from django.db import models

# Create your models here.


class phone_test(models.Model):
    #id = models.CharField(max_length=30,verbose_name='id')
    phone = models.CharField(max_length=30,verbose_name='手机号')
    country = models.CharField(max_length=30,verbose_name='国家(默认为+86)')
    information_url = models.CharField(max_length=1000,verbose_name='跳转到短信url')
    source = models.CharField(max_length=100,verbose_name='来源网站')
    Creation_time = models.CharField(max_length=30,verbose_name='创建时间')

class gps_position(models.Model):
    phone_models=models.CharField(max_length=1000,verbose_name='手机型号')
    title=models.CharField(max_length=1000,verbose_name='标题')
    content=models.CharField(max_length=1000,verbose_name='内容')
    longitude = models.CharField(max_length=1000, verbose_name='经度')
    latitude = models.CharField(max_length=1000, verbose_name='纬度')
    detailed_address = models.CharField(max_length=1000, verbose_name='详细地址')
    time=models.CharField(max_length=500,verbose_name='时间戳')
    creation_time = models.CharField(max_length=1000, verbose_name='创建时间')