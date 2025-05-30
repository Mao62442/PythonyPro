from django.db import models

class Department(models.Model):
    title = models.CharField(verbose_name='部門タイトル',max_length=32)

class User(models.Model):
    name = models.CharField(verbose_name='名前',max_length=32)
    age = models.IntegerField(verbose_name='年齢')
    salary = models.IntegerField(verbose_name='給料')

    depart = models.ForeignKey(verbose_name='関連部門',to='Department',on_delete=models.CASCADE)