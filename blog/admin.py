from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, Category, Comment, Tag

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
