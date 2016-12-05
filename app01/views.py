#coding:utf-8
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from models import *
from AccountForm import LoginForm, Regis

# Create your views here.

def index(request):
    users = UserProfile.objects.all()
    return render_to_response('index.html',{'users':users})

def Login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']            
            password = form.cleaned_data['password']
            result = UserProfile.objects.filter(UserName=username, PassWord=password).count()
            if result == 1:
                return redirect('/')
                
            #print data['username'], data['password'] 
                #return HttpResponse('登录成功')
    else:
        form = LoginForm()
    return render_to_response('Login.html', {'form':form}, context_instance=RequestContext(request))

def UserList(request):
    users = UserProfile.objects.all()    
    return render_to_response('UserList.html',{'users':users})


def regis(request):
    if request.method == 'POST':
        form = Regis(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            #验证用户是否已经存在。
            result = UserProfile.objects.filter(UserName=username).count()
            if result == 1:
                return HttpResponse('你已经注册， 不能重复注册。')
            #数据入库
            UserProfile.objects.create(UserName=username, PassWord=password)
            #print username, password
            return HttpResponse('注册成功')
    else:
        form = Regis()
    return render_to_response('regis.html',{'form':form}, context_instance=RequestContext(request))

  

def UserDetail(request,uid):
    uid = int(uid)
    user = UserProfile.objects.get(id=uid)
    print type(user)
    return render_to_response('userdetail.html', {'user':user})


def Delete(request,uid):
    UserProfile.objects.filter(id=uid).delete()
    return redirect('/')
def testPage(request):
    return render_to_response('demo.html')


