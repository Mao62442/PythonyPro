from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name="ユーザー名",max_length=32)
    password = models.CharField(verbose_name="パスワード",max_length=32)
    age = models.IntegerField(verbose_name="年齢")
    mobileNumber = models.CharField(verbose_name="年齢",max_length=11)