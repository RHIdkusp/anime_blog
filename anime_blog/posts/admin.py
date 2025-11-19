from django.contrib import admin
from .models import Post, Comment, Category

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_at')
    search_fields = ('title', 'content')
    
admin.site.register(Comment)

admin.site.register(Post)
admin.site.register(Category)