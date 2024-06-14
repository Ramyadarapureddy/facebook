from django.contrib import admin

from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
# Register your models here.
admin.site.register(models.Post, PostAdmin)