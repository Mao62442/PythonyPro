from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name="ユーザー名",max_length=32)
    password = models.CharField(verbose_name="パスワード",max_length=32)
    age = models.IntegerField(verbose_name="年齢")
    mobileNumber = models.CharField(verbose_name="年齢",max_length=11)

class Department(models.Model):
    title = models.CharField(verbose_name="タイトル",max_length=32)

class User(models.Model):
    name = models.CharField(verbose_name="名前",max_length=12)
    age = models.IntegerField(verbose_name="年齢")
    salary = models.IntegerField(verbose_name="給料")
    depart = models.ForeignKey(verbose_name="部署",to="Department",on_delete=models.CASCADE)