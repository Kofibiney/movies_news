from django.contrib import admin

# Register your models here.
from .models import Category,News,Comment,Upcoming

admin.site.register(Category)


class AdminNews(admin.ModelAdmin):
    list_display=('title','category','add_time')

admin.site.register(News,AdminNews)

class AdminUpcoming(admin.ModelAdmin):
    list_display=('title','category','add_time')

admin.site.register(Upcoming,AdminUpcoming)


class AdminComment(admin.ModelAdmin):
    list_display=('news','email','comment','status')

admin.site.register(Comment,AdminComment)