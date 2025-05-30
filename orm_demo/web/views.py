from django.shortcuts import render,redirect
from web import models

def user_list(request):
    '''
        select user.id, user.name, user.age, user.salary, department.title
        from web_user as user
        left join web_department as department
        on user.depart_id = department.id
    '''
    querySet = models.User.objects.all()

    # queryStr = "select user.id, user.name, user.age, user.salary, department.title from web_user as user left join web_department as department on user.depart_id = department.id"
    # userList = models.User.objects.raw(queryStr)

    # SQL文の実行結果を画面ファイルに返す
    return render(request, 'user_list.html', {"querySet": querySet})
    # return render(request, 'user_list.html', {"querySet": userList})

def add_user(request):
    # すべての部門を取得
    if request.method == "GET":
        departList  = models.Department.objects.all()
        return render(request, 'add_user.html', {"departList": departList})
    # ユーザーの追加処理
    name = request.POST.get("name")
    age = request.POST.get("age")
    salary = request.POST.get("salary")
    depart_id = request.POST.get("depart")
    models.User.objects.create(name=name, age=age, salary=salary, depart_id=depart_id)
    return redirect("/user/list")