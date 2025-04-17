from django.shortcuts import render, HttpResponse, redirect
from app import models

# Create your views here.
def depart(request):
    # ORM操作

    # データー登録
    # models.Department.objects.create(title="営業部",count=20)
    # models.Department.objects.create(**{"title":"総務部","count":"5"})
    # models.Department.objects.create(**{"title":"技術部","count":"15"})
    # models.Department.objects.create(**{"title":"設計部","count":"15"})

    # データー検索
    # 全件検索
    # queryset = models.Department.objects.all()
    # 条件検索
    # queryset = models.Department.objects.filter(id__gt=1) # id > 1
    # obj = models.Department.objects.filter(id=1).first() # id = 1
    # for obj in queryset:
    # print(obj.id, obj.title, obj.count)

    # データー削除
    # models.Department.objects.filter(id=4).delete() # id = 4

    # データー更新
    # models.Department.objects.filter(id=5).update(count=99)

    # 全件検索
    # departList = models.Department.objects.all().order_by("-id") # desc
    departList = models.Department.objects.all().order_by("id") # asc

    return render(request, 'depart.html', {"departList":departList})

def add_depart(request):
    if request.method == "GET":
        return render(request,'add_depart.html')
    else:
        id = request.POST.get("id")
        title = request.POST.get("title")
        count = request.POST.get("count")
        models.Department.objects.create(id=id, title=title, count=count)
        return redirect("/depart/")

def delete_depart(request):
    depart_id = request.GET.get('id')
    models.Department.objects.filter(id=depart_id).delete()
    return redirect("/depart/")

def edit_depart(request):
    if request.method == "GET":
        depart_id = request.GET.get('id')
        depart_object = models.Department.objects.filter(id=depart_id).first()
        return render(request, 'edit_depart.html', {"depart_object":depart_object})
    else:
        depart_id = request.GET.get('id')
        edit_title = request.POST.get('title')
        edit_count = request.POST.get('count')
        models.Department.objects.filter(id=depart_id).update(title=edit_title,count=edit_count)
        return redirect("/depart/")