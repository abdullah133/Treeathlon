from django.contrib import admin
from .models import Post, SideWidget





@admin.register(SideWidget)
class SideWidgetAdmin(admin.ModelAdmin):
    list_display = ['title','content',]
    # def has_add_permission(self, request):
    #   return False
    #
    #
    # def has_delete_permission(self, request, obj=None):
    #   return False
    #

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','date_posted']
