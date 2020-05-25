from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse # Add this
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from . models import ContactAdressen, ContactUsInfo
# Create your views here.
def contactgeschafftview(request):
    return render(request, 'contact_app/contact_geschafft.html', {})

def contactview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            print('ja ich habs geschaft')
            betreff = form.cleaned_data['betreff']
            email_from= form.cleaned_data['email']
            nachricht_from = form.cleaned_data['nachricht']
            name = form.cleaned_data['name']
            msg_html = render_to_string('contact_form_email.html', {'betreff':betreff,
                                                                    'email_from':email_from,
                                                                    'nachricht_from':nachricht_from,
                                                                    'name': name,})
            from_email = settings.DEFAULT_FROM_EMAIL
            users_email = 'eagle.golden50@gmail.com'
            to_list = [users_email]
            subject = 'hallo'
            message = 'text version'
            send_mail(subject=subject,message=message, from_email=from_email, recipient_list=to_list,html_message=msg_html,)

            return redirect('contact_app:contact_success_page')
    else:
        form = ContactForm()
        adressen = ContactAdressen.objects.all()
        contact_info = ContactUsInfo.objects.all()

    context = {'form':form,
               'adressen':adressen,
               'contact_info':contact_info,
                }

    return render(request, 'contact_app/contact.html', context = context)
