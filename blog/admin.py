from django.contrib import admin
from .models import Post, PostImages


class PostImagesInline(admin.TabularInline):
	model = PostImages
	extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	inlines = [PostImagesInline]


@admin.register(PostImages)
class PostImagesAdmin(admin.ModelAdmin):
    pass