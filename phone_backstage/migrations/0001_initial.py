# Generated by Django 3.1.1 on 2021-01-25 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gps_position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_models', models.CharField(max_length=1000, verbose_name='手机型号')),
                ('title', models.CharField(max_length=1000, verbose_name='标题')),
                ('content', models.CharField(max_length=1000, verbose_name='内容')),
                ('longitude', models.CharField(max_length=1000, verbose_name='经度')),
                ('latitude', models.CharField(max_length=1000, verbose_name='纬度')),
                ('detailed_address', models.CharField(max_length=1000, verbose_name='详细地址')),
                ('time', models.CharField(max_length=500, verbose_name='时间戳')),
                ('creation_time', models.CharField(max_length=1000, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='phone_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30, verbose_name='手机号')),
                ('country', models.CharField(max_length=30, verbose_name='国家(默认为+86)')),
                ('information_url', models.CharField(max_length=1000, verbose_name='跳转到短信url')),
                ('source', models.CharField(max_length=100, verbose_name='来源网站')),
                ('Creation_time', models.CharField(max_length=30, verbose_name='创建时间')),
            ],
        ),
    ]
