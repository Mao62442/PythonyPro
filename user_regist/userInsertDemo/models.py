from django.db import models

class UserInfo(models.Model):
    username = models.CharField(verbose_name="ユーザー名", max_length=32)
    password = models.CharField(verbose_name="パスワード", max_length=64)
    age = models.IntegerField(verbose_name="年齢")

class Department(models.Model):
    title = models.CharField(verbose_name="部署名", max_length=32)
    count = models.IntegerField(verbose_name="人　数")