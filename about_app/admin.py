from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Team, ContactInfo, TeamDescription


@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin):
    pass


class TeamDescriptionaAdmin(admin.ModelAdmin):
    list_display = ('title','content')

    # def has_add_permission(self, request):
    #   return False
    #
    #
    # def has_delete_permission(self, request, obj=None):
    #   return False

class ContactInfoAdmin(admin.ModelAdmin):

    # def has_add_permission(self, request):
    #   return False
    #
    #
    # def has_delete_permission(self, request, obj=None):
    #   return False


admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(TeamDescription, TeamDescriptionaAdmin)
