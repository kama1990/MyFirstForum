from django.contrib import admin
from .models import Posts
# Register your models here.


# we added here date to admin - when date was created
class CreateDate(admin.ModelAdmin):
    readonly_fields=('createDate',)

admin.site.register(Posts, CreateDate)