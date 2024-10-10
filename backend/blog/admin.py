from django.contrib import admin
from .models import Poem, Question, PostCategory, Post, PostViews, PoemTheme


admin.site.register(Poem)
admin.site.register(Question)
admin.site.register(PostCategory)
admin.site.register(PoemTheme)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {"slug": ["title"]}
    search_fields = ['post']

@admin.register(PostViews)
class PostViewsAdmin(admin.ModelAdmin):
    list_display = ['post', 'ip_address']