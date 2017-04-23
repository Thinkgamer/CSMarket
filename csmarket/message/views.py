#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from message.models import Message,Cate,Mwords
import time
from django.core.files.storage import FileSystemStorage
from logre.models import User
# Create your views here.

#发布需求/服务
@csrf_exempt
def postService(request,cate):
    if request.method == 'POST':
        title = request.POST.get('biaoti')
        #保存图片，以url形式存储到数据库中
        image = request.FILES["fengmian"]
        fs = FileSystemStorage()
        filename = fs.save("fengmian/"+image.name, image)
        uploaded_file_url = fs.url(filename)

        leibie = request.POST.get('leibie')
        price = request.POST.get('baojia')
        miaoshu = request.POST.get('miaoshu')

        if Message.objects.filter(mess_title=title,mess_author=request.user):
            return render_to_response('post_service.html',{
                'user_name': request.user,
                'cate': cate,
                'title': title,
                'leibie': leibie,
                'price': price,
                'miaoshu': miaoshu,
                'repeat_error': '你已发表过该标题的需求或者服务！'
            })

        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        mess = Message(mess_title=title,mess_image=uploaded_file_url,mess_author=request.user,mess_time=now_time,\
                       mess_xuorfu=cate,mess_price=price,mess_seenum=0,mess_content=miaoshu)
        mess.mess_cate_id=Cate.objects.get(cate_name=leibie).cate_num
        mess.save()

        return HttpResponseRedirect("/message/oneService/%s/%s" % (request.user,title))
        # return render_to_response('services_one.html', {
        #     'user_name': request.user,
        #     'cate': cate,
        #     'flag': 1 if cate == "服务" else 0,
        # })
    else:
        if request.user.is_authenticated:
            return render_to_response('post_service.html',{
                'user_name': request.user,
                'cate': cate,
            })
        else:
            request.session['error'] = "你还没有登录，请先登录！"
            try:
                referer = request.META['HTTP_REFERER']  # 获取网页访问来源
                return HttpResponseRedirect(referer)
            except:
                return render_to_response('404.html',{
                    'error':request.session.get('error',default=None)
                })
#编辑需求
def editService(request,cate):

    return render_to_response("edit_service.html",{
        'cate': cate,
    })

#查看单个需求或者服务
def oneService(request,user,title):
    # 获取该title对应的message的信息
    one = Message.objects.get(mess_title=title,mess_author=user)
    one.mess_seenum = one.mess_seenum + 1
    one.save()
    # 获取该message对应的发布者的联系信息
    per = User.objects.get(username=one.mess_author)
    return render_to_response('services_one.html',{
        'user_name': user,
        'title': one.mess_title,
        'fengmian': one.mess_image,
        'smallcate': one.mess_cate,
        'price': one.mess_price,
        'time': one.mess_time,
        'author': one.mess_author,
        'seenum': one.mess_seenum,
        'tuo': one.mess_hezuo,
        'iforno': one.mess_ifsuccess,
        'cate': one.mess_xuorfu,
        'content': one.mess_content,
        'wechat': per.user_wechat,
        'qq': per.user_qq,
        'phone': per.user_phone,
    })


#查看服务商库/需求大厅/代办中心
def allService(request,cate):
    # cate
    if cate=="需求":
        title_name = "需求大厅"
    elif cate=="服务":
        title_name = "服务商库"
    else:
        title_name = "代办中心"
    # 分页
    mess_list = Message.objects.filter(mess_xuorfu=cate).order_by("-mess_time")
    paginator = Paginator(mess_list, 10)  # Show 20 contacts per page
    page = request.GET.get('page')
    try:
        all_mess = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_mess = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_mess = paginator.page(paginator.num_pages)

    return render_to_response('supmarket.html',{
        'user_name': request.user,
        "len_list": range(1, paginator.num_pages+1),
        "all_mess": all_mess,
        'title_name': title_name,
    })