from django.contrib import admin

from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','user','post','text')
# Register your models here.
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)