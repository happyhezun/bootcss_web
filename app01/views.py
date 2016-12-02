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
            UserProfile.objects.create(UserName=username, PassWord=password)
            #print username, password
            return HttpResponse('注册成功')
    else:
        form = Regis()
    return render_to_response('regis.html',{'form':form}, context_instance=RequestContext(request))

def edit(request, id):
    id= int(id)
    users = UserProfile.objects.filter(id=id)
    return render_to_response('edit.html',{'form':users})
    pass

def testPage(request):
    return render_to_response('demo.html')


