from django.contrib import admin

from blog.models import Comment, Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'author',
        'likes',
        'tags',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'post',
        'author',
    )
    list_display = (
        'id',
        'post',
        'author',
        'text',
        'published_at',
    )


admin.site.register(Tag)