from django.contrib import admin
from .models import Events
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
# Register your models here.

def printen(modeladmin, request, queryset):

    for obj in queryset:
        print('obj:'+str(obj))



        msg_html = render_to_string('base_app/email_vorlagen/bewertungsaufforderung_email.html', {'obj':obj,})
        from_email = settings.DEFAULT_FROM_EMAIL



        users_email = obj.email
        print('users_email:'+str(users_email))
        print('users_email:'+str(users_email))
        print('users_email:'+str(users_email))
        print('users_email:'+str(users_email))
        print('users_email:'+str(users_email))


        an_dennis = 'dennis.am90@gmail.com'

        to_list = [an_dennis]
        send_mail(subject=subject,message=message, from_email=from_email, recipient_list=to_list,html_message=msg_html,)
        obj.update(nachricht_verschickt=True)





class EventsAdmin(admin.ModelAdmin):
    list_display = ['id','title','image_tag',]
    list_editable = ['title',]
    actions = [printen,]

printen.short_description = "Printen juhuhuhuhuhuhuuhuhuhuh"


admin.site.register(Events, EventsAdmin)
