from django.contrib import admin
from .models import ContactAdressen, ContactUsInfo
# Register your models here.



class ContactUsInfoAdmin(admin.ModelAdmin):
    list_display = ('title','content')

    # def has_add_permission(self, request):
    #   return False
    #
    #
    # def has_delete_permission(self, request, obj=None):
    #   return False

class ContactAdmin(admin.ModelAdmin):
    list_display = ('adresse','telefon', 'email')

    # def has_add_permission(self, request):
    #   return False
    #
    #
    # def has_delete_permission(self, request, obj=None):
    #   return False

admin.site.register(ContactAdressen, ContactAdmin)
admin.site.register(ContactUsInfo, ContactUsInfoAdmin)
