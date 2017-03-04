#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from logre.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

# Create your views here.
@csrf_exempt
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pwd=request.POST.get('passwd')
        # print(request.user.is_authenticated())
        user = authenticate(email=email, password=pwd)
        if user is not None:
            return render_to_response('usermanager.html',{

            })
        else:
            return render_to_response('login.html',{
                'error': '邮箱或者密码错误！',
                'tag': 1,
                'user_email': email,
                'user_pwd': pwd,
            })
    else:
        return render_to_response('login.html',{
            'tag':1,
        })


def usermanager(request):
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
        "len_list": range(1, paginator.num_pages),
    })


def more(request,uname):
    user=User.objects.get(username=uname)
    return render_to_response('usermanager.html',{
        'tag':1,
        'user': user,
    })

def through(reqest,uname):
    user = User.objects.get(username=uname)
    user.user_isValid=True
    user.save()
    return HttpResponseRedirect('/manager/usermanager/')

@csrf_exempt
def send(request,email):
    if request.method=='POST':
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        from manager.send_email import sendEmail
        result=sendEmail(email,subject,content)  #result=1
        return HttpResponseRedirect('/manager/usermanager/')
    else:
        return render_to_response('sendemail.html',{
            'email': email,
        })