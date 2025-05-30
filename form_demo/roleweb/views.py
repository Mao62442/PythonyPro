from django.core.validators import RegexValidator
from django.http import HttpResponse
from django.shortcuts import render
from django import forms

class RoleForm(forms.Form):
    user = forms.CharField(
        label='名前',
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9]+$',
                message='半角英数字のみ使用可能です',
                code='invalid_username'
            )
        ]
    )
    password = forms.CharField(
        label='パスワード',
        max_length=100,
        widget=forms.PasswordInput()
    )
    email = forms.EmailField(
        label='メールアドレス',
        required=False,
        widget=forms.EmailInput()
    )
    city = forms.ChoiceField(
        label='都道府県',
        choices=[
            ('1', '東京'),
            ('2', '大阪'),
            ('3', '京都'),
            ('4', '奈良'),
            ('5', '福岡'),
        ]
    )
def add_role(request):
    if request.method == 'GET':
        form = RoleForm()
        return render(request, 'add_role.html',  {'form': form})
    form = RoleForm(data=request.POST)
    if form.is_valid():
        print("成功",form.cleaned_data)
        return HttpResponse("成功")
    else:
        print("失敗",form.errors)
        return render(request, 'add_role.html',  {'form': form})