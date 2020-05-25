from django.contrib import admin
from .models import PartnerInfo, PartnerDescription
# Register your models here.
admin.site.register(PartnerInfo)


@admin.register(PartnerDescription)
class PartnerDescriptionAdmin(admin.ModelAdmin):
    list_display = ['title',]

    # def has_add_permission(self, request):
    #   return False
    #
    #
    # def has_delete_permission(self, request, obj=None):
    #   return False
