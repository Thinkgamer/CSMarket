#-*- coding: utf-8-*-
from django.shortcuts import render,render_to_response
from news.models import News,cate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def all(request,newcate):
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
    paginator = Paginator(new_list, 20)  # Show 20 contacts per page
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
        'csmdongtai': csmdongtai,
        'chuangke': chuangke,
        'catename': newcate,
        'all_new': all_new,
        "len_list": range(1, paginator.num_pages+1),
    })


def one(request,newtitle):
    if request.method=='POST':
        pass
    else:
        new=News.objects.get(new_title=newtitle)
        if new.new_cate_id==1:
            csmdongtai = False;chuangke = True
        elif new.new_cate_id==2:
            csmdongtai = True;chuangke = False
        return render_to_response('news_one.html',{
            'new': new,
            'csmdongtai': csmdongtai,
            'chuangke': chuangke,
            'title': newtitle,
        })