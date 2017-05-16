# CSMarket
University student trading platform<br>
大学生交易平台

---

# 简介
这是一个基于Django的网站，主要是为了大学生创造一个创意交易平台和代办平台，如果你也对这个项目感兴趣的话，你可以联系我.
<br>
我的联系方式是：<br>
微信: gyt13342445911<br>
QQ: 1923361654<br>
邮箱: thinkgamer@163.com<br>

---

# 环境说明
系统: Ubuntu 16.04<br>
python: python3.5<br>
Django: 1.10.4<br>
Mysql 5.7.17(并没有使用内嵌的sqlite)<br>
data目录: 数据库文件备份<br>
数据库备份： /usr/bin/mysqldump -uusername -ppassword databasename  --default-character-set=utf8 --opt -Q -R >./csmarket.sql<br>
数据库恢复： /usr/bin/mysql -uusername -ppassword databasename --default-character-set=utf8 <./csmarket.sql<br> 
后台登录的账号和密码是： thinkgamer  csmarket <br>

## pymysql
安装 : pip3 install pymysql<br>
在项目的__init__.py文件中加入以下内容 :
```
import pymysql  
pymysql.install_as_MySQLdb()
```
## kindeditor
<a href="http://blog.csdn.net/gamer_gyt/article/details/66598750">后台中引入富文本编辑器</a><br>


---
# 备注
1：<a href='http://blog.csdn.net/gamer_gyt/article/details/60466842'>user扩展方式是AbstractUser</a><br>
2: 遇到问题 
>module 'django.views' has no attribute 'static'

解决办法：先把出错的地方注释掉，同步数据库后在解除掉注释

---

>django request.FILES MultiValueDictKeyError 

解决办法：form 表单中添加 enctype="multipart/form-data

> django model 中的或查询

解决办法： Q对象查询，http://blog.csdn.net/heybob/article/details/50547552

3：Django教程
<a href='http://blog.csdn.net/column/details/12861.html'>Django 从零开始到项目优化</a>
