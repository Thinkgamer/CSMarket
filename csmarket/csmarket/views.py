#-*-coding:utf-8 -*-
from news.models import cate,News
from message.models import Message
from django.shortcuts import render_to_response

def index(request):
    #CSM动态 = 2  创客故事= 1
    csm_list = News.objects.filter(new_cate=2).order_by("-new_time")
    ck_list = News.objects.filter(new_cate=1).order_by("-new_time")

    #最新需求列表
    xuqiu_list = Message.objects.filter(mess_xuorfu="需求").order_by("-mess_time")

    #最服务列表
    fuwu_list = Message.objects.filter(mess_xuorfu="服务").order_by("-mess_time")

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
            'xuqiu_list': xuqiu_list[:12],
            'fuwu_list': fuwu_list[:12],
            'error': error,
        })
    else:
        return render_to_response('index.html', {
            'csm_list': csm_list[:5],
            'ck_list': ck_list[:5],
            'xuqiu_list': xuqiu_list[:10],
            'fuwu_list': fuwu_list[:12],
            'error': error,
        })