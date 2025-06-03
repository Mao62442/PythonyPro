from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from userInsertDemo import models

# Formの実装し方
class LoginForm(forms.Form):
    username = forms.CharField(
        label='ユーザー名',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ユーザー名'})
    )
    password = forms.CharField(
        label='パスワード',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'パスワード'})
    )

# ModelFormの実装し方
class LoginModelFom(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        # fields = ['username', 'password']
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ユーザー名'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'パスワード'}),
        }

class DepartModelForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = '__all__'
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        # user_object = models.UserInfo.objects.filter(
        #     username=form.cleaned_data['username'],
        #     password=form.cleaned_data['password']
        # ).first()
        user_object = models.UserInfo.objects.filter(**form.cleaned_data).first()
        if user_object:
            request.session['username'] = user_object.username
            return HttpResponse('ログイン成功')
        else:
            return render(request, 'login.html', {'form': form, 'error': 'ユーザー名またはパスワード不正'})
    else:
        return render(request, 'login.html', {'form': form})

def depart_list(request):
    # 部門一覧を取得
    querySet = models.Department.objects.all()
    return render(request, 'depart_list.html', {'querySet': querySet})

def add_depart(request):
    if request.method == 'GET':
        form = DepartModelForm()
        return render(request, 'depart_form.html', {'form': form})
    form = DepartModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/depart/list/')
    else:
        return render(request, 'depart_form.html', {'form': form})

def delete_depart(request):
    did = request.GET.get("did")
    models.Department.objects.filter(id=did).delete()
    return redirect('/depart/list/')

def edit_depart(request):

    did = request.GET.get("did")
    depart_object = models.Department.objects.filter(id=did).first()

    if request.method == 'GET':
        form = DepartModelForm(instance=depart_object)
        return render(request, 'depart_form.html', {'form': form})

    form = DepartModelForm(data=request.POST, instance=depart_object)

    if form.is_valid():
        form.save()
        return redirect('/depart/list/')
    else:
        return render(request, 'depart_form.html', {'form': form})