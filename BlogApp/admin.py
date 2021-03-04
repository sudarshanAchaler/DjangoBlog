from django.contrib import admin
from .models import Post, Comment, PostDraft

# Register your models here.

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinymce.js',)


admin.site.register(Comment)
admin.site.register(PostDraft)