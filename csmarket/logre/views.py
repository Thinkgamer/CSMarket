#-*-coding: utf-8-*-
from django.shortcuts import render_to_response,render
from django.views.decorators.csrf import csrf_exempt
from logre.models import UserProfile,User
from django.http import HttpResponseRedirect
import time
# Create your views here.

#用户登录
@csrf_exempt
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pwd=request.POST.get('passwd')
        user = User.objects.filter(email=email)
        #如果邮箱存在
        if len(user)!=0:
            if user[0].password==pwd:
                # return render_to_response("prefect.html", {
                # })
                #更新最后登录时间
                now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                user.update(last_login=now_time)
                return HttpResponseRedirect('/logre/prefect/')
            else:
                return render_to_response("login.html", {
                    "error": "密码不正确！",
                    'user_email': email,
                })
        #如果邮箱不存在
        else:
            return render_to_response("login.html", {
                "error": "邮箱不存在！",
                'user_email': email,
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
        user = User(username=username, password=pwd, email=email,last_login=now_time)
        user.save()
        return HttpResponseRedirect('/logre/prefect/')

    else:
        return render_to_response("register.html",{

        })

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
        imgfile1 = request.POST.get('imgfile1')
        imgfile2 = request.POST.get('imgfile2')
        #信息补充
        wechat = request.POST.get('wechat')
        qq = request.POST.get('qq')
        shanchang = request.POST.get('shanchang')
        xuanyan = request.POST.get('xuanyan')

        pass
    else:
        return render_to_response('prefect.html',{

        })