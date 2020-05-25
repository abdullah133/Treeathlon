from django.contrib import admin
from .models import Privacy

# Register your models here.
@admin.register(Privacy)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ['title',]
