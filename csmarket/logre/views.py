#-*-coding: utf-8-*-
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from logre.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from message.models import Message,DMessage
from django.core.files.storage import FileSystemStorage
import time
# Create your views here.

#用户登录
@csrf_exempt
def login(request):
    global referer
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
            try:
                return HttpResponseRedirect(referer)
            except:
                return HttpResponseRedirect("/index/")
        else:
            return render_to_response('login.html',{
                'error': '邮箱或者密码不正确',
                'user_name': uname,
                'user_pwd': pwd,
            })
    else:
        try:
            referer = request.META['HTTP_REFERER']  # 获取网页访问来源
        except:
            pass
        finally:
            return render_to_response('login.html',{})


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
    auth_logout(request)
    try:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    except:
        return HttpResponseRedirect("/")

#完善个人信息
@csrf_exempt
def prefect(request):
    if request.method=='POST':
        phone = request.POST.get('phone')
        # 学生身份认证信息
        eid = request.POST.get('eid')
        school = request.POST.get('school')
        startyear = request.POST.get('startyear')
        jinianzhi = request.POST.get('jinianzhi')
        xueli = request.POST.get('xueli')
        xuehao = request.POST.get('xuehao')
        # imgfile = request.POST.get('imgfile')
        #信息补充
        wechat = request.POST.get('wechat')
        qq = request.POST.get('qq')
        shanchang = request.POST.get('shanchang')
        xuanyan = request.POST.get('xuanyan')

        # 保存图片，以url形式存储到数据库中
        image = request.FILES["imgfile"]
        fs = FileSystemStorage()
        filename = fs.save("xszimg/" + image.name, image)
        uploaded_file_url = fs.url(filename)

        #保存信息
        user = User.objects.get(username=request.user)
        user.user_phone = phone
        user.user_eid = eid
        user.user_school = school
        user.user_start_year = startyear
        user.user_year = jinianzhi
        user.user_xueli = xueli
        user.user_xuehao = xuehao
        user.user_xszimg = uploaded_file_url
        user.user_wechat = wechat
        user.user_qq = qq
        user.user_shanchang = shanchang
        user.user_xuanyan = xuanyan

        user.save()

        if request.user.is_authenticated:
            user_name = request.user
        else:
            user_name = ''

        return render_to_response('index.html',{
            'user_name': user_name,
        })
    else:
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
        else:
            user =''

        return render_to_response('prefect.html',{
            'user': user,
        })

def personal(request):

    # 判断用户名
    if request.user.is_authenticated:
        user_name = request.user
        user = User.objects.get(username=user_name)

        # 需求
        xuqiu_list = Message.objects.filter(mess_xuorfu="需求", mess_author=user_name)[:5]
        # 服务
        fuwu_list = Message.objects.filter(mess_xuorfu="服务", mess_author=user_name)[:5]
        # 代办
        daiban_list = DMessage.objects.filter(dmess_author=user_name)[:5]

        return render_to_response('personal.html', {
            'user_name': user_name,
            'user': user,
            'xuqiu_list': xuqiu_list,
            'fuwu_list': fuwu_list,
            'daiban_list': daiban_list,
        })
    else:
        error = '你还没有登录，请先登录'
        return render_to_response('personal.html',{
            'error': error,
        })
