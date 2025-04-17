from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(verbose_name="名前", max_length=16)
    age = models.IntegerField(verbose_name="年齢")
    # password = models.CharField(verbose_name="パスワード",max_length=64, null=True,blank=True)
    password = models.CharField(verbose_name="パスワード",max_length=64, default="123456")
    email = models.CharField(verbose_name="メールアドレス", max_length=32)
