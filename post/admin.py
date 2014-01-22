from post.models import Post, Comment
from django.contrib import admin


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['post']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]
    list_filter = ['pub_date']
    search_fields = ['post']
    date_hierarchy = 'pub_date'


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
