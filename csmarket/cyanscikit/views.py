# coding: utf8
from django.shortcuts import render_to_response
from cyanscikit.models import doc as Doc
from cyanscikit.models import example as Example
# Create your views here.

def index(request):

    # 获取技术文档列表
    doc_list = Doc.objects.all().order_by('-pub_date')[:5]

    # 获取案例列表
    exam_list = Example.objects.all().order_by('-pub_date')[:8]

    if request.COOKIES.get('name',''):
        user_name = request.COOKIES.get('name','')
    else:
        user_name = ''

    return render_to_response('cyanscikit.html', {
        'user_name': user_name,
        'doc_list': doc_list,
        'exam_list': exam_list,
    })

# 案例展示
def example(request):

    # example
    exam_list = Example.objects.all().order_by('-pub_date')

    if request.COOKIES.get('name',''):
        user_name = request.COOKIES.get('name','')
    else:
        user_name = ''

    return render_to_response('cs_example.html',{
        'user_name': user_name,
        'exam_list': exam_list,
    })

# 单个案例
def oneexample(request, title_):

    # one example
    exa = Example.objects.get(title=title_)
    exa.see_num += 1
    exa.save()

    if request.COOKIES.get('name',''):
        user_name = request.COOKIES.get('name','')
    else:
        user_name = ''
    return render_to_response('cs_example_one.html',{
        'user_name': user_name,
        'exa': exa,
    })

# 技术文档
def doc(request):
    # 获取技术文档列表
    doc_list = Doc.objects.all().order_by('-pub_date')

    if request.request.COOKIES.get('name',''):
        user_name = request.COOKIES.get('name','')
    else:
        user_name = ''
    return render_to_response('cs_docmore.html', {
        'user_name': user_name,
        'doc_list': doc_list,
    })

#单个技术文档
def onedoc(request, title_):

    # one doc
    doc = Doc.objects.get(title=title_)
    doc.see_num += 1
    doc.save()

    # 热门推荐
    hot_list = Doc.objects.exclude(title = title_).order_by('-see_num')

    if request.COOKIES.get('name',''):
        user_name = request.COOKIES.get('name','')
    else:
        user_name = ''
    return render_to_response('cs_doc_one.html',{
        'user_name': user_name,
        'hot_list': hot_list,
        'doc': doc,
    })