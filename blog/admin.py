from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ("likes", )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
