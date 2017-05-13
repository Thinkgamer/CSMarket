#-*-coding:utf-8 -*-
from news.models import cate,News
from message.models import Message,DMessage
from django.shortcuts import render_to_response
from cyanscikit.models import example

def index(request):
    # 清除 request.error
    try:
        del request.session['error']
    except:
        pass
    #CSM动态 = 2  创客故事= 1
    csm_list = News.objects.filter(new_cate=2).order_by("-new_time")[:5]
    ck_list = News.objects.filter(new_cate=1).order_by("-new_time")[:5]

    # 案例中心
    exam_list = example.objects.all().order_by("-pub_date")[:5]

    # 急需代办
    daiban_list = DMessage.objects.all().order_by('-dmess_time')

    #最新需求列表
    xuqiu_list = Message.objects.filter(mess_xuorfu="需求").order_by("-mess_time")[:12]

    #最服务列表
    fuwu_list = Message.objects.filter(mess_xuorfu="服务").order_by("-mess_time")[:12]

    #凡是需要登录进行的操作，都会先检查是否登录，未登录，则将错误写到session中，在此进行判断
    error = request.session.get('error',default=None)
    try:
        del request.session['error']
    except:
        pass

    # if request.user.is_authenticated:
    if request.COOKIES.get('name',''):
        return render_to_response('index.html',{
            # 'user_name':request.user,
            'user_name': request.COOKIES.get('name',''),
            'csm_list': csm_list,
            'exam_list': exam_list,
            'ck_list': ck_list,
            'xuqiu_list': xuqiu_list,
            'fuwu_list': fuwu_list,
            'daiban_list': daiban_list,
            'error': error,
        })
    else:
        return render_to_response('index.html', {
            'csm_list': csm_list,
            'ck_list': ck_list,
            'exam_list': exam_list,
            'xuqiu_list': xuqiu_list,
            'fuwu_list': fuwu_list,
            'daiban_list': daiban_list,
            'error': error,
        })