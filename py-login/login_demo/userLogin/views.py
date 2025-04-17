from django.shortcuts import render, redirect
from userLogin import models

# Create your views here.
def userlogin(request):
    if request.method == "GET":
        return render(request, 'login.html')

    user = request.POST.get('user')
    pwd = request.POST.get('password')

    user_object = models.UserInfo.objects.filter(username=user, password=pwd).first()
    if user_object:
        """
        下記のように実装
            1.随時文字列作成
            2.作成した文字列をCookieに格納
            3.文字列 + ユーザー識別をSessionに格納
        """
        request.session["info"] = {
            "id": user_object.id,
            "username": user_object.username,
            "password": user_object.password,
            "mobileNumber": user_object.mobileNumber
        }
        return redirect("/home/")
    else:
        return render(request, 'login.html', {'error':'ユーザー名或いはパスワード不正'})

def home(request):
    info_session = request.session.get("info")
    if not info_session:
        return render(request, 'login.html')
    return render(request,"home.html",{"info_session":info_session})