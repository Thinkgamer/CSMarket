#-*- coding: utf-8-*-
from django.shortcuts import render,render_to_response
from news.models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def all(request):
    new_list = News.objects.all().order_by("-new_time")
    paginator = Paginator(new_list, 1)  # Show 20 contacts per page
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
        'all_new': all_new,
        "len_list": range(1, paginator.num_pages),
    })


def one(request):
    return render_to_response('news_one.html',{

    })