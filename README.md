# phone
This is an online project to receive authentication codes

1.寻找在线接收认证码的网站（至今遇见有两种，一种是加密的，另一种是为加密。先好没有加密的【其实加密与不加密都没有什么关系】）

2.利用爬虫进行爬虫相关的数据（已经爬取一个网站的数据存入数据库内，其他的网站还在找。。）

3.编写后台接口（前端暂时为安卓app端，）

4.编写安卓app前端（自己打包成功的有kivy，还有一个pyqt5，但是没有打包成功。暂时有kivy编写前端代码）

5.git在其他电脑上拉取代码时需要做以下操作
    5.1需要新创建ssh—key密钥$ ssh-keygen -t rsa -C "你自己注册GitHub的邮箱" 
    5.2执行这个命令$ ssh -T git@github.com会报错也不管他
    5.3运行pycharm登录git
    5.4从git拉取代码报错 Clone failed: Unable to access 'https://github.com/yanhailin666/phone.git/': SSL certificate problem: unable to get local issuer certificate
    5.5这个时候在桌面右击鼠标，点击git bash bere进入
    5.6然后输入git config --global http.sslVerify false命令运行
    5.7如果在登录git账号时预见404或者没有提示没有权限时，可以使用token进行登录
6.使用说明
    6.1打开VCS先lmport into Version Control》选择Share Project on GitHub进行带出git的信息
    6.2打开VSC点击git找到clone进行点击，进入选择GitHub，选择好目录进行拉取
    
7.该项目需要安装跨域问题，所以需要安装pip install django-cors-headers 跨域库，不然运行项目会报错

8.一键生成该项目需要的库 pip freeze > requirements.txt 迁移安装库 pip install -r requirements.txt

9.python运行命令
    1.数据库
    python manage.py makemigrations
    python manage.py migrate
    
10.HBuilderX需要导入css插件（不然项目运行不了）
    网站为：https://ext.dcloud.net.cn/plugin?name=compile-node-sass