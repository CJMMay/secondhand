from django.shortcuts import render,render_to_response
from .models import User
from django import forms
from django.http import HttpResponseRedirect
# Create your views here.

class UserForm(forms.Form):
    stuid = forms.CharField(label = '账号 :',max_length = 15)
    password = forms.CharField(label = '密码 :',widget = forms.PasswordInput())

def login(request):
    if request.method=='POST':
        uf=UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            stuid = uf.cleaned_data['stuid']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(stuid__exact = stuid,password__exact = password)
            if user:
                return render_to_response('detail.html',{'stuid':stuid})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()  
    return render_to_response('login.html',{'uf':uf}) 

def changepwd(request):
    return render(request,'changepwd')
def register(request):
    return render(request,'register')