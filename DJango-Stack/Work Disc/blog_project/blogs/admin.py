from django.contrib import admin
from .models import Blog, Comment, Admin as BlogAdmin

# Register your models here.

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(BlogAdmin)