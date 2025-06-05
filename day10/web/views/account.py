from io import BytesIO

from django import forms
from django.shortcuts import render,HttpResponse,redirect

from web import models
from utils.encrypt import md5
from utils.helper import check_code

class LoginForm(forms.Form):
    username = forms.CharField(
        label='ユーザー名',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ユーザー名'})
    )
    password = forms.CharField(
        label='パスワード',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'パスワード'},
        render_value=True)
    )
    code = forms.CharField(
        label='認証コード',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '認証コード'})
    )

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    form = LoginForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'login.html', {'form': form})
    # 認証コードを確認する
    image_code = request.session.get('img_code')
    if not image_code:
        form.add_error('code', '認証コード有効期限切れ')
        return render(request, 'login.html', {'form': form})
    if image_code.upper() != form.cleaned_data['code'].upper():
        form.add_error('code', '認証コードが間違っています')
        return render(request, 'login.html', {'form': form})

    user = form.cleaned_data['username']
    password = form.cleaned_data['password']
    encrypt_password = md5(password)
    admin_object = models.Admin.objects.filter(username=user,password=encrypt_password).first()
    if not admin_object:
        return render(request, 'login.html', {'form': form, 'error':"ユーザー名或はパスワード不正"})
    request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
    request.session.set_expiry(60 * 60 * 24 * 7)
    return redirect("/home/")

def logout(request):
    request.session.clear()
    return redirect('/login/')

def img_code(request):
    # 1.図を作成する
    image_object, code_str = check_code()
    # 2.図の内容を返す
    stream = BytesIO()
    image_object.save(stream, 'png')
    stream.getvalue()

    request.session['img_code'] = code_str
    request.session.set_expiry(60)

    return HttpResponse(stream.getvalue(), 'image/png')

def home(request):
    request.info_dict['name']
    return render(request, 'home.html')