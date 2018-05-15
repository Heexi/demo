# 商城案例

## 安装依赖包

`pip install - r requirements.txt`

## 安装redis

`sudo apt-get install redis-server`

## 安装数据库

`sudo apt-get install mysql5.6`

### 创建数据库用户

`grant all on *.* to 'django'@'%' identified by 'djangopwd'`

### 创建数据库

`create database shop`

## 数据库迁移

`./manage.py makemigrations && ./manage.py migrate` 

## 启动服务器

`./manage.py runserver`

