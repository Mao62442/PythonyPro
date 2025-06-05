from django import forms
from django.http import JsonResponse
from django.shortcuts import render, redirect

from web import models
from utils.encrypt import md5

def admin_list(request):
    queryset = models.Admin.objects.all().order_by("id")
    return render(request, 'admin_list.html', {"queryset": queryset})

class AdminModelForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field_object in self.fields.items():
            if name == 'password':
                field_object.widget = forms.PasswordInput(attrs={'class': 'form-control'})
            field_object.widget.attrs = {"class": "form-control"}

def admin_add(request):
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, 'admin_form.html', {"form": form})
    form = AdminModelForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'admin_form.html', {"form": form})
    form.instance.password = md5(form.instance.password)
    form.save()
    return redirect('/admin/list/')


class AdminEditModelForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = ['username', 'age', 'gender', 'department']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field_object in self.fields.items():
            field_object.widget.attrs = {"class": "form-control"}

def admin_edit(request, id):
    admin_object = models.Admin.objects.filter(id=id).first()
    if request.method == "GET":
        form = AdminEditModelForm(instance=admin_object)
        return render(request, 'admin_form.html', {"form": form})
    form = AdminEditModelForm(data=request.POST, instance=admin_object)
    if not form.is_valid():
        return render(request, 'admin_form.html', {"form": form})
    form.save()
    return redirect('/admin/list/')

def admin_delete(request):
    id = request.GET.get('id')
    models.Admin.objects.filter(id=id).delete()
    return JsonResponse({"status": True})