from django.contrib import admin
from .models import Join, BeschreibungenHomeSeite, Vision, TreeathlonInZahlen, BackgroundImgDescription
from import_export.admin import ImportExportModelAdmin

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
# admin.site.register(Join)


class BeschreibungenHomeSeiteAdmin(admin.ModelAdmin):
    list_display = ('title','description')

    def has_add_permission(self, request):
      return False


    def has_delete_permission(self, request, obj=None):
      return False

class VisionAdmin(admin.ModelAdmin):
    list_display = ('title','description')

    def has_add_permission(self, request):
      return False


    def has_delete_permission(self, request, obj=None):
      return False

class TreeathlonInZahlenAdmin(admin.ModelAdmin):
    list_display = ('title','spenden_number', 'content')
    def has_add_permission(self, request):
      return False


    def has_delete_permission(self, request, obj=None):
      return False

class BackgroundImgDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    def has_add_permission(self, request):
      return False


    def has_delete_permission(self, request, obj=None):
      return False



admin.site.register(BeschreibungenHomeSeite, BeschreibungenHomeSeiteAdmin)
admin.site.register(Vision, VisionAdmin)
admin.site.register(TreeathlonInZahlen, TreeathlonInZahlenAdmin)
admin.site.register(BackgroundImgDescription, BackgroundImgDescriptionAdmin)

# Register your models here.
# هاد الشي مهم للأدمن مشان اذا بدي ابعت ايميل او هيك شي
# def printen(modeladmin, request, queryset):
#     subject = 'UNDIS freut sich über eine Bewertung!'
#     message = 'UNDIS freut sich über eine Bewertung von dir!!'
#     for obj in queryset:
#         print('obj:'+str(obj))
#
#
#
#         msg_html = render_to_string('base_app/email_vorlagen/meinemail.html', {'obj':obj,})
#         from_email = settings.DEFAULT_FROM_EMAIL
#
#
#
#         users_email = obj.email
#         print('users_email:'+str(users_email))
#         print('users_email:'+str(users_email))
#         print('users_email:'+str(users_email))
#         print('users_email:'+str(users_email))
#         print('users_email:'+str(users_email))
#
#
#         an_dennis = 'dennis.am90@gmail.com'
#
#         to_list = [an_dennis]
#         send_mail(subject=subject,message=message, from_email=from_email, recipient_list=to_list,html_message=msg_html,)
#
#
#
#
#
# class JoinAdmin(admin.ModelAdmin):
#     list_display = ['id','email','timestamp',]
#
#     actions = [printen,]
#
# printen.short_description = "Printen juhuhuhuhuhuhuuhuhuhuh"
@admin.register(Join)
class JoinAdmin(ImportExportModelAdmin):
    list_display = ['email','timestamp',]
