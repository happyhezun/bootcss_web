#coding:utf-8
'''
Created on 2016年12月1日

@author: Turing
'''
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    #PassWord = forms.CharField(widget=forms.PasswordInput,required = False)
    

class Regis(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.IntegerField(min_value=1)
    address = forms.CharField(widget=forms.Textarea)

    