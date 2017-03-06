#-*-coding:utf-8 -*-

from django.shortcuts import render_to_response

def index(request):
    if request.user.is_authenticated:
        return render_to_response('index.html',{
            'user_name':request.user,
        })
    else:
        return render_to_response('index.html', {
        })