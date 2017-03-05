#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from logre.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
import time

# Create your views here.
@csrf_exempt
def login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pwd=request.POST.get('passwd')
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            auth_login(request, user)
            # 更新最后登录时间
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            user.last_login=now_time
            user.save()
            return HttpResponseRedirect('/manager/usermanager/')
        else:
            return render_to_response('login.html',{
                'error': '邮箱或者密码不正确',
                'user_name': uname,
                'user_pwd': pwd,
                'tag':1,
            })
    else:
        return render_to_response('login.html',{
            'tag':1,
        })

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/manager/login/')

def usermanager(request):
    if request.user:
        user_list = User.objects.filter(user_isValid=False).order_by("-date_joined")
        paginator = Paginator(user_list, 20)  # Show 20 contacts per page
        page = request.GET.get('page')
        try:
            all_user = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            all_user = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            all_user = paginator.page(paginator.num_pages)
        return render(request, 'usermanager.html', {
            'tag':0,
            'all_user': all_user,
            "len_list": range(1, paginator.num_pages+1),
            'user_name': request.user,
        })
    else:
        return render_to_response('login.html', {
            'error': '你还没有登录',
        })

#查看更多信息
def more(request,uname):
    if request.user:
        user=User.objects.get(username=uname)
        return render_to_response('usermanager.html',{
            'tag':1,
            'user': user,
            'user_name': request.user,
        })
    else:
        return render_to_response('login.html',{
            'error': '你还没有登录',
        })

#通过验证
def through(request,uname):
    if request.user:
        user = User.objects.get(username=uname)
        user.user_isValid=True
        user.save()
        return HttpResponseRedirect('/manager/usermanager/')
    else:
        return render_to_response('login.html', {
            'error': '你还没有登录',
        })

#如果注册数据有问题执行发送邮件
@csrf_exempt
def send(request,email):
    if request.user:
        if request.method=='POST':
            subject = request.POST.get('subject')
            content = request.POST.get('content')
            from manager.send_email import sendEmail
            result=sendEmail(email,subject,content)  #result=1
            return HttpResponseRedirect('/manager/usermanager/')
        else:
            return render_to_response('sendemail.html',{
                'email': email,
                'user_name': request.user,
            })
    else:
        return render_to_response('login.html', {
            'error': '你还没有登录',
        })