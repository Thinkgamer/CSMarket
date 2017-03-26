#-*-coding:utf-8 -*-
from news.models import cate,News

from django.shortcuts import render_to_response

def index(request):
    #CSM动态 = 2  创客故事= 1
    csm_list = News.objects.filter(new_cate=2).order_by("-new_time")
    ck_list = News.objects.filter(new_cate=1).order_by("-new_time")

    #凡是需要登录进行的操作，都会先检查是否登录，未登录，则将错误写到session中，在此进行判断
    error = request.session.get('error',default=None)
    try:
        del request.session['error']
    except:
        pass

    if request.user.is_authenticated:
        return render_to_response('index.html',{
            'user_name':request.user,
            'csm_list': csm_list[:5],
            'ck_list': ck_list[:5],
            'error': error,
        })
    else:
        return render_to_response('index.html', {
            'csm_list': csm_list[:5],
            'ck_list': ck_list[:5],
            'error': error,
        })