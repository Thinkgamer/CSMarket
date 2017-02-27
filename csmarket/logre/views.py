#-*-coding: utf-8-*-
from django.shortcuts import render_to_response,render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#用户登录
@csrf_exempt
def login(request):
    return render_to_response('login.html',{

    })

#用户注册
@csrf_exempt
def register(request):
    return render_to_response("register.html",{

    })

#完善个人信息
@csrf_exempt
def prefect(request):
    return render_to_response('prefect.html',{

    })