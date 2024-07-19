# blog/admin.py
from django.contrib import admin
from .models import Post, Category, Tag, Author


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'categories')
    list_display_links = ('id', 'title', 'author', 'categories')
    list_filter = ('author', 'categories')
    search_fields = ('title',)
    filter_horizontal = ('tags',)
