
from django.shortcuts import render, render_to_response,redirect
from .models import User
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import HttpResponse
# Create your views here.
# 显示注册页面
def res(request):
    try:
        del request.session['error']
    except:
        return render(request, 'res.html')
    return render(request, 'res.html')


# 注册操作
def do_res(request):
    stuid = request.POST.get('stuid')
    if not User.objects.filter(stuid=stuid):
        password = request.POST.get('password')
        username = request.POST.get('username')
        tele = request.POST.get('tele')
        class1 =request.POST.get('class1')
        major =request.POST.get('major')
        sex = request.POST.get('sex')
        User.objects.create(stuid=stuid,password=password,username=username,tele=tele,class1=class1,major=major,sex=sex)
        return redirect(reverse('login_res:login'))  # 注册成功，重定向到登录页面
    else:
        request.session['error'] = '用户已存在'
        con = {
            'stuid': request.POST.get('stuid'),
            'password': request.POST.get('password'),
        }
        return render(request, 'res.html', con)



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
                request.session['stuid'] =stuid
                return render_to_response('sells/product/home.html', {'stuid': stuid})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})


def xinxi(request):
    stuid=request.session['stuid']
    lists=User.objects.get(stuid=stuid)
    con={
        "list":lists,
        "stuid":lists.stuid,
        "username":lists.username,
        "sex":lists.sex,
        "age":lists.age,
        "tele":lists.tele,
        "eml":lists.eml,
        "jianjie":lists.jianjie,
    }
    return render(request,'xinxi.html',con)
 
#保存个人信息
def do_xinxi(request):
    stuid=request.POST.get('stuid')
    username=request.POST.get('username')
    sex=request.POST.get('sex')
    age=request.POST.get('age')
    tele=request.POST.get('tele')
    eml=request.POST.get('eml')
    jianjie=request.POST.get('jianjie')
    res=User.objects.filter(stuid=stuid).update(username=username,sex=sex,age=age,tele=tele,eml=eml,jianjie=jianjie)
    if res:
        con={
            
            'suss':'修改成功'
        }
        # return render(request,'login_res/xinxi.html')
        return redirect(reverse('login_res:xinxi'),con)
    else:
        return HttpResponse('修改失败')