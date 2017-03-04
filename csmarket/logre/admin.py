from django.contrib import admin
from logre.models import User
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

