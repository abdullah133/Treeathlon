from django.contrib import admin
from .models import Teilnahme, SpendeDescription
# Register your models here.
@admin.register(Teilnahme)
class TeilnahmeAdmin(admin.ModelAdmin):
    list_display = ['vorname','date_posted',]
    ordering = ['-date_posted']


@admin.register(SpendeDescription)
class SpendeDescriptionAdmin(admin.ModelAdmin):
    list_display = ['title',]


    def has_add_permission(self, request):
      return False


    def has_delete_permission(self, request, obj=None):
      return False
