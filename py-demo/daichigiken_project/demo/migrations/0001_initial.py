# Generated by Django 5.2 on 2025-04-15 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='名前')),
                ('age', models.IntegerField(verbose_name='年齢')),
                ('email', models.CharField(max_length=32, verbose_name='メールアドレス')),
            ],
        ),
    ]
