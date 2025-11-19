from django.contrib import admin
from .models import Post
from .models import Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_at')
    search_fields = ('title', 'content')
    
admin.site.register(Comment)