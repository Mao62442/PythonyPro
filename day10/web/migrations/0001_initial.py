# Generated by Django 5.2.1 on 2025-06-03 02:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='部門')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='名前')),
                ('password', models.CharField(max_length=64, verbose_name='パスワード')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年齢')),
                ('gender', models.CharField(choices=[(1, '男性'), (2, '女性')], max_length=1, verbose_name='性別')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.department', verbose_name='部門')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='電話番号')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='価格')),
                ('level', models.SmallIntegerField(choices=[(1, '1級'), (1, '2級'), (1, '3級'), (1, '4級')], default=1, verbose_name='レベル')),
                ('status', models.SmallIntegerField(choices=[(1, '使用済'), (2, '未使用')], default=2, verbose_name='ステータス')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.admin', verbose_name='管理人')),
            ],
        ),
    ]
