#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.contrib.auth import authenticate
# Create your views here.

#发布需求/服务
def postService(request,cate):
    if request.user.is_authenticated:
        return render_to_response('post_service.html',{
            'cate': cate,
            'flag': 1 if cate=="服务" else 0,
        })
    else:
        request.session['error'] = "你还没有登录，请先登录！"
        referer = request.META['HTTP_REFERER']  # 获取网页访问来源
        return HttpResponseRedirect(referer)

#编辑需求
def editService(request,cate):

    return render_to_response("edit_service.html",{
        'cate': cate,
        'flag': 1 if cate == "服务" else 0,
    })