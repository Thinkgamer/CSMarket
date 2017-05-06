# coding: utf8
from django.shortcuts import render,render_to_response

# Create your views here.

def index(request):

    if request.user.is_authenticated:
        user_name = request.user
    else:
        user_name = ''

    return render_to_response('cyanscikit.html', {
        'user_name': user_name,
    })

# 案例展示
def example(request):

    if request.user.is_authenticated:
        user_name = request.user
    else:
        user_name = ''

    return render_to_response('cs_example.html',{

    })

# 单个案例
def oneexample(request):

    if request.user.is_authenticated:
        user_name = request.user
    else:
        user_name = ''
    return render_to_response('cs_example_one.html',{

    })

# 技术文档
def doc(request):

    if request.user.is_authenticated:
        user_name = request.user
    else:
        user_name = ''
    return render_to_response('cs_docmore.html', {

    })

#单个技术文档
def onedoc(request):

    if request.user.is_authenticated:
        user_name = request.user
    else:
        user_name = ''
    return render_to_response('cs_doc_one.html',{

    })