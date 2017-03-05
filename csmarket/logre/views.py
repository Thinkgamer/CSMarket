#-*-coding: utf-8-*-
from django.shortcuts import render_to_response,render
from django.views.decorators.csrf import csrf_exempt
from logre.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
import time
# Create your views here.

#用户登录
@csrf_exempt
def login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pwd=request.POST.get('passwd')
        user = authenticate(username=uname,password=pwd)
        if user is not None:
            auth_login(request, user)
            # 更新最后登录时间
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            user.last_login=now_time
            user.save()
            return HttpResponseRedirect('/logre/prefect/')
        else:
            return render_to_response('login.html',{
                'error': '邮箱或者密码不正确',
                'user_name': uname,
                'user_pwd': pwd,
            })
    else:
        return render_to_response('login.html',{

        })


#用户注册
@csrf_exempt
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('passwd')
        if User.objects.filter(username=username,email=email):
            return render_to_response('register.html', {
                'username': username,
                'email': email,
                'pwd': pwd,
                'error': '你输入的邮箱和用户名已存在',
            })
        elif User.objects.filter(username=username):
            return render_to_response('register.html', {
                'username': username,
                'email': email,
                'pwd': pwd,
                'error': '你输入的用户名已存在',
            })
        elif User.objects.filter(email=email):
            return render_to_response('register.html',{
                'username': username,
                'email': email,
                'pwd': pwd,
                'error': '你输入的邮箱已存在'
            })
        # 将新注册的用户存入数据库
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        user=User.objects.create_user(username=username,email=email,password=pwd)
        user.last_login=now_time
        user.save()

        return HttpResponseRedirect('/logre/prefect/')

    else:
        return render_to_response("register.html",{

        })

def logout(request):
    pass

#完善个人信息
@csrf_exempt
def prefect(request):
    if request.method=='POST':
        phone = request.POST.get('phpne')
        # 学生身份认证信息
        eid = request.POST.get('eid')
        school = request.POST.get('school')
        startyear = request.POST.get('startyear')
        jinianzhi = request.POST.get('jinianzhi')
        xueli = request.POST.get('xueli')
        xuehao = request.POST.get('xuehao')
        imgfile = request.POST.get('imgfile')
        #信息补充
        wechat = request.POST.get('wechat')
        qq = request.POST.get('qq')
        shanchang = request.POST.get('shanchang')
        xuanyan = request.POST.get('xuanyan')

        pass
    else:
        return render_to_response('prefect.html',{
        })