from django.contrib import admin
from .models import Posts, PostComment
# Register your models here.


# we added here date to admin - when date was created
class CreateDate(admin.ModelAdmin):
    readonly_fields=('createDate',)

admin.site.register(Posts, CreateDate)
admin.site.register(PostComment)



# @admin.register(PostComment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'content', 'post', 'createDate', 'active')
#     list_filter = ('active', 'createDate')
#     search_fields = ('user', 'content')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)
