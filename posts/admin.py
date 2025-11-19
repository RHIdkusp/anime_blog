from django.contrib import admin
from .models import Post, Comment, Category

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_at')
    search_fields = ('title', 'content')
    filter_horizontal = ('categories',)
    
admin.site.register(Comment)

admin.site.register(Category)