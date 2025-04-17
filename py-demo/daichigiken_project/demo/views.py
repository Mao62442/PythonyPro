from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('user')
        password = request.POST.get('password')
        if username == 'root' and password == '123456':
            return redirect('/index/')
        else:
            return render(request, 'login.html', {"error" : "ユーザー名或いはパスワード不正"})

def index(request):
    phoneList = [
        {"id": 1, "brand": "Apple", "place": "America"},
        {"id": 2, "brand": "Samsung", "place": "Korea"},
        {"id": 3, "brand": "Sony", "place": "Japan"},
        {"id": 4, "brand": "Vivo", "place": "China"}
    ]

    return render(request, 'index.html', {"phoneList": phoneList})