#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from logre.models import UserProfile,User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def usermanager(request):
    if request.method=='POST':
        pass
    else:
        user_list = User.objects.filter(userprofile__user_isValid=None).order_by("-date_joined")
        # paginator = Paginator(user_list, 12)  # Show 25 contacts per page
        # page = request.GET.get('page')
        # page = request.GET.get('page')
        # try:
        #     all_user = paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     all_user = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     all_user = paginator.page(paginator.num_pages)
        # return render(request, 'usermanager.html', {
        #     'all_user': all_user,
        #     "len_list": range(1, paginator.num_pages),
        # })
        return render_to_response('usermanager.html',{
            'user_list': user_list,
            'count_num': len(user_list),
        })