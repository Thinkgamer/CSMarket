from django.contrib import admin
from logre.models import User,UserSee
# Register your models here.

#将UserProfile加入到Admin的user表中
# class ProfileInline(admin.StackedInline):
#     model = UserProfile
#     verbose_name = 'profile'
#
# class UserProfileAdmin(admin.ModelAdmin):
#     # list_display = ('username', 'email', 'user_phone', 'date_joined','last_login',)
#     # search_fields = ('username', 'email', 'user_phone', 'date_joined','last_login','user_qq','user_wechat','user_school',)
#     # list_filter = ('date_joined', 'user_school','user_year',)
#     # ordering = ('-date_joined',)
#
#     inlines = (ProfileInline,)

#去掉在admin中的注册
# admin.site.unregister(User)

#用userProfileAdmin注册user
admin.site.register(User)

class AdminUserSee(admin.ModelAdmin):
    list_display = ('title','pub_author','see_people','cate','time',)
    search_fields =('title','pub_author','see_people','cate',)
    list_filter = ('title','pub_author','see_people','cate',)
    ordering = ('-time',)

admin.site.register(UserSee,AdminUserSee)