from django.contrib import admin

# Register your models here.
from django.contrib import admin

from articleapp.models import Campaign, Article, PriceCategory, ArticleCategory


@admin.register(Campaign)
class PostAdmin(admin.ModelAdmin):
    list_display = ['participants_id', 'amount', 'article_id', 'state']
    list_display_links = ['state']


@admin.register(Article)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'writer', 'created_at', 'price', 'total_amount','receipt','hit']


@admin.register(PriceCategory)
class PostAdmin(admin.ModelAdmin):
    list_display = ['article', 'food', 'clothing', 'shelter']
    list_display_links = ['article']

@admin.register(ArticleCategory)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']
