from django.contrib import admin
from core.models import Post

class CreatedTime(admin.ModelAdmin):
    readonly = ('date',)
    
admin.site.register(Post, CreatedTime)
