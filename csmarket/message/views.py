#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from message.models import Message,Cate,Mwords,DMwords,DMessage,DCate
import time
from django.core.files.storage import FileSystemStorage
from logre.models import User,UserSee
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

        # 这里要根据类别来定，因为服务/需求 是公用一个数据表， 而代办中心是一个单独的数据表
        if cate=="代办":
            bool_rep = DMessage.objects.filter(dmess_title=title, dmess_author=request.COOKIES.get('name'))
        else:
            bool_rep = Message.objects.filter(mess_title=title, mess_author=request.COOKIES.get('name'))

        if bool_rep:
            if Message.objects.filter(mess_title=title,mess_author=request.COOKIES.get('name')):
                return render_to_response('post_service.html',{
                    'user_name': request.COOKIES.get('name'),
                    'cate': cate,
                    'title': title,
                    'leibie': leibie,
                    'price': price,
                    'miaoshu': miaoshu,
                    'repeat_error': '你已发表过该标题的需求或者服务！'
                })

        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        #根据类别来判断映射那哪个数据库模型
        if cate == "代办":
            mess = DMessage(dmess_title=title, dmess_image=uploaded_file_url, dmess_author=request.COOKIES.get('name'), dmess_time=now_time, \
                           dmess_price=price, dmess_seenum=0, dmess_content=miaoshu)
            mess.dmess_cate_id = DCate.objects.get(dcate_name=leibie).dcate_num
        else:
            mess = Message(mess_title=title,mess_image=uploaded_file_url,mess_author=request.COOKIES.get('name'),mess_time=now_time,\
                       mess_xuorfu=cate,mess_price=price,mess_seenum=0,mess_content=miaoshu)
            mess.mess_cate_id=Cate.objects.get(cate_name=leibie).cate_num
        mess.save()

        return HttpResponseRedirect("/message/oneService/%s/%s/%s" % (request.COOKIES.get('name'),cate,title))
        # return render_to_response('services_one.html', {
        #     'user_name': request.user,
        #     'cate': cate,
        #     'flag': 1 if cate == "服务" else 0,
        # })
    else:
        uname = request.COOKIES.get('name','')
        user = User.objects.get(username=uname)
        # 如果用户已经被认证，且已经审核通过
        if user and user.user_isValid:
            cate_list =DCate.objects.all() if cate=="代办" else Cate.objects.all()
            return render_to_response('post_service.html',{
                'user_name': request.COOKIES.get('name'),
                'cate': cate,
                'cate_list': cate_list,
            })
        # 如果未通过审核，提示先去补充个人信息
        elif not user.user_isValid:
            request.session['not_auth_error'] = "你还没有进行信息认证，请先去认证信息"
            try:
                referer = request.META['HTTP_REFERER']  # 获取网页访问来源
                return render_to_response('prefect.html', {
                    'not_auth_error': '你还没有通过信息认证，请完善或者修改信息!',
                    'referer': referer,
                    'user': User.objects.get(username=request.COOKIES.get('name','')),
                })
            except:
                return render_to_response('404.html', {
                    'error': request.session.get('not_auth_error', default=None)
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
def edit(request,cate,title):

    return render_to_response("edit_service.html",{
        'cate': cate,
        'title': title,
    })

#删除信息
def delete(request,cate,title):
    if cate=='代办':
        DMessage.objects.get(dmess_author=request.COOKIES.get('name'),dmess_title=title).delete()
    else:
        Message.objects.get(mess_author=request.COOKIES.get('name'),mess_title=title).delete()
    return HttpResponseRedirect('/index')

#查看单个需求或者服务
def oneService(request,user,cate,title):
    # 记录浏览信息
    if request.COOKIES.get('name',''):
        see_name = request.COOKIES.get('name','')
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 查询message 表中的image
        if cate=='代办':
            image = DMessage.objects.get(dmess_author=user,dmess_title=title).dmess_image
        else:
            image = Message.objects.get(mess_author=user,mess_title=title).mess_image
        # 如果已经浏览过，则更新即可
        try:
            if UserSee.objects.get(title=title, see_people=see_name):
                see_update = UserSee.objects.get(title=title, see_people=see_name)
                see_update.time = now_time
                see_update.save()
        except:
            see = UserSee(title=title,image=image,pub_author=user,see_people=see_name,cate=cate,time=now_time)
            see.save()

    # 获取该title对应的message的信息
    if cate == "代办":
        one = DMessage.objects.get(dmess_title=title, dmess_author=user)
        one.dmess_seenum = one.dmess_seenum + 1
        one.save()
        # 获取该message对应的发布者的联系信息
        per = User.objects.get(username=one.dmess_author)
    else:
        one = Message.objects.get(mess_title=title,mess_author=user)
        one.mess_seenum = one.mess_seenum + 1
        one.save()
        # 获取该message对应的发布者的联系信息
        per = User.objects.get(username=one.mess_author)

    if request.COOKIES.get('name')==user:
        flag= 1
    return render_to_response('services_one.html',{
        'user_name': request.COOKIES.get('name',''),
        'title': one.dmess_title if cate=="代办" else one.mess_title,
        'fengmian': one.dmess_image if cate=="代办" else one.mess_image,
        'smallcate': one.dmess_cate if cate=="代办" else one.mess_cate,
        'price': one.dmess_price if cate=="代办" else one.mess_price,
        'time': one.dmess_time if cate=="代办" else one.mess_time,
        'author': one.dmess_author if cate=="代办" else one.mess_author,
        'seenum': one.dmess_seenum if cate=="代办" else one.mess_seenum,
        'tuo': one.dmess_hezuo if cate=="代办" else one.mess_hezuo,
        'iforno': one.dmess_ifsuccess if cate=="代办" else one.mess_ifsuccess,
        'cate': cate,
        'content': one.dmess_content if cate=="代办" else one.mess_content,
        'wechat': per.user_wechat,
        'qq': per.user_qq,
        'phone': per.user_phone,
        'flag': 1 if request.COOKIES.get('name')==user else 0,
    })


#查看服务商库/需求大厅/代办中心
def allService(request,cate):
    # cate
    if cate=="需求":
        title_name = "需求大厅"
        cate_list = Cate.objects.all().order_by('cate_num')
    elif cate=="服务":
        title_name = "服务商库"
        cate_list = Cate.objects.all().order_by('cate_num')
    else:
        title_name = "代办中心"
        cate_list = DCate.objects.all().order_by('dcate_num')
    # 分页
    if cate=="代办":
        mess_list = DMessage.objects.all().order_by("-dmess_time")
    else:
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
        'user_name': request.COOKIES.get('name',''),
        "len_list": range(1, paginator.num_pages+1),
        "all_mess": all_mess,
        'title_name': title_name,
        'cate': cate,
        'cate_list': cate_list,
    })

def Onecate(request,cate,onecate):
    # onecate 为小类别  cate 为 服务，需求，代办中的一个
    if cate=='代办':
        mess_list = DMessage.objects.filter(dmess_cate__dcate_name=onecate).order_by("-dmess_time")
        cate_list = DCate.objects.all().order_by('dcate_num')
    else:
        mess_list = Message.objects.filter(mess_cate__cate_name=onecate).order_by("-mess_time")
        cate_list = Cate.objects.all().order_by('cate_num')

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
        'user_name': request.COOKIES.get('name',''),
        "len_list": range(1, paginator.num_pages + 1),
        "all_mess": all_mess,
        'cate': cate,
        'cate_list': cate_list,
        'title_name': onecate,
    })