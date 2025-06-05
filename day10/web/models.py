from django.db import models

# 部門表
class Department(models.Model):
    title = models.CharField(verbose_name="部門",max_length=16)
    def __str__(self):
        return self.title

# 社員表
class Admin(models.Model):
    GENDER_CHOICES = [
        (1, "男"),
        (2, "女"),
    ]
    username = models.CharField(verbose_name="名前",max_length=20)
    password = models.CharField(verbose_name="パスワード",max_length=64)
    age = models.IntegerField(verbose_name="年齢",null=True,blank=True)
    gender = models.IntegerField(verbose_name="性別",choices=GENDER_CHOICES)
    department = models.ForeignKey(verbose_name="部門",to="Department",on_delete=models.CASCADE)

# 電話番号表
class Phone(models.Model):
    mobile = models.CharField(verbose_name="電話番号",max_length=11)
    # 符号なし、正値のみ
    price = models.PositiveIntegerField(verbose_name="価格",default=0)
    level = models.SmallIntegerField(
        verbose_name="レベル",
        choices=[
            (1, "1級"),
            (1, "2級"),
            (1, "3級"),
            (1, "4級")
        ],
        default=1
    )

    status_choice = (
        (1, "使用済"),
        (2, "未使用")
    )

    status = models.SmallIntegerField(verbose_name="ステータス",choices=status_choice,default=2)
    admin = models.ForeignKey(verbose_name="管理人",to="Admin",on_delete=models.CASCADE)