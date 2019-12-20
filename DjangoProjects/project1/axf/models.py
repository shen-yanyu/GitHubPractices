from django.db import models

# Create your models here.
# python manage.py makemigrations  此时数据库还没有生成数据表
# python manage.py migrate
# python manage.py runserver
# 创建数据库和写入读取数据


class Wheel(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)
    isDelte = models.BooleanField(default=False)