from django.contrib import admin
from .models import Blog_details

class blog_detials_new(admin.ModelAdmin):
    fields=['user','title','descrription']
    list_display=('user','title','date_pub','time_stamp')

admin.site.register(Blog_details,blog_detials_new)
