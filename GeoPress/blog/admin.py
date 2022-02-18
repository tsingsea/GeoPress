from django.contrib import admin

# Register your models here.
from .models import Article, Category, Tag, ArticleUpDown, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_author', 'post_pub_date', 'post_mod_date', 'post_title', 'post_body', 'category']
    list_display_links = list_display

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ArticleUpDown)
admin.site.register(Comment)