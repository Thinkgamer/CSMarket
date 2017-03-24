#-*- coding: utf-8-*-
from django.shortcuts import render,render_to_response
from news.models import News,cate,Words
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
import time
# Create your views here.
def all(request,newcate):
    if request.user.is_authenticated:
        user_name=request.user
    else:
        user_name=''
    #这里传进来的应该是分类的名字
    #new_cate=2 代表是CSM动态,  1 代表是创客故事
    cate_id=cate.objects.get(cate_name=newcate).id
    if cate_id==1:
        csmdongtai=False;chuangke=True
    elif cate_id==2:
        chuangke=False;csmdongtai=True
    else:
        pass
    new_list = News.objects.filter(new_cate=cate_id).order_by("-new_time")
    paginator = Paginator(new_list, 15)  # Show 20 contacts per page
    page = request.GET.get('page')
    try:
        all_new = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_new = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_new = paginator.page(paginator.num_pages)
    return render(request, 'news.html', {
        'user_name': user_name,
        'csmdongtai': csmdongtai,
        'chuangke': chuangke,
        'catename': newcate,
        'all_new': all_new,
        "len_list": range(1, paginator.num_pages+1),
    })

@csrf_exempt
def one(request,newid):
    #验证用户
    if request.user.is_authenticated:
        user_name=request.user
    else:
        user_name=''

    #获取该篇文章的相关信息
    new = News.objects.get(id=newid)
    new.new_seenum = new.new_seenum + 1
    new.save()
    if new.new_cate_id == 1:
        csmdongtai = False;chuangke = True
    elif new.new_cate_id == 2:
        csmdongtai = True;chuangke = False
    #获取评论信息
    mess_list = Words.objects.filter(new_id=newid).order_by("-m_time")
    #热门推荐列表  __lt  实现不等于
    hot_list = News.objects.filter(id__lt = newid).order_by('-new_seenum')[:5]
    #是否是post请求
    if request.method=='POST':
        #如果用户已经登录，存储评论信息
        if user_name:
            content = request.POST.get('talk')
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            mess = Words(new_id=newid,m_content=content,father_id=-1,m_time=now_time,m_people=user_name)
            mess.save()
            return render_to_response('news_one.html', {
                'user_name': user_name,
                'new': new,
                'csmdongtai': csmdongtai,
                'chuangke': chuangke,
                'title': new.new_title,
                'mess_list': mess_list,
                'hot_list': hot_list,
            })
        #如果用户未登录，则返回并提示登录
        else:
            return render_to_response('news_one.html', {
                'user_name': user_name,
                'new': new,
                'csmdongtai': csmdongtai,
                'chuangke': chuangke,
                'title': new.new_title,
                'mess_list':mess_list,
                'hot_list': hot_list,
                'error': '你还没有登录,是否去登录',
            })
    else:
        return render_to_response('news_one.html',{
            'user_name': user_name,
            'new': new,
            'csmdongtai': csmdongtai,
            'chuangke': chuangke,
            'title': new.new_title,
            'hot_list': hot_list,
            'mess_list':mess_list,
        })