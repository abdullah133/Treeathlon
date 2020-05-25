from django.shortcuts import render, redirect
from .forms import TeilnahmeForm, FrageForm
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView
from .models import Teilnahme
from .multiforms import MultiFormsView

from django.http import HttpResponse, HttpResponseRedirect


class MultipleFormsDemoView(MultiFormsView):

    template_name = "spenden_app/spenden.html"
    form_classes = {'teilnahme_form': TeilnahmeForm,
                    'frage_form': FrageForm,}
    success_urls = {
        'teilnahme_form': reverse_lazy('spenden_app:spenden_page'),
        'frage_form': reverse_lazy('spenden_app:spenden_page'),
    }
    meine_leere_liste = dict()



    def frage_form_form_valid(self, form):

        cd = form.cleaned_data

        meine_frage = cd['frage']
        meine_frage_2 = cd['frage_2']
        meine_frage_3 = cd['frage_3']
        meine_frage_4 = cd['frage_4']
        print('meine_frage:'+str(meine_frage))
        mein_ergebnis = meine_frage*meine_frage_2
        mein_ergebnis_2 = meine_frage*1000
        # form.instance.ergebnis = mein_ergebnis_2    das ist für model form also für modal

        self.meine_leere_liste['mein_ergebnis'] = mein_ergebnis
        self.meine_leere_liste['mein_zweites_ergebnis'] = mein_ergebnis_2 #hier habe ich eine Frage über mein_zweites_ergebnis in diesem satz
        form_name = form.cleaned_data.get('action')
        return HttpResponseRedirect(self.get_success_url(form_name))

    def get_context_data(self, **kwargs):
        context = super(MultipleFormsDemoView, self).get_context_data(**kwargs)
        context['mein_zusatz_context'] = self.meine_leere_liste
        context['mein_header_bild'] = 'spenden-banner-area relative'

        return context

    def teilnahme_form_form_valid(self, form):
        print(self.meine_leere_liste)
        form_name = form.cleaned_data.get('action')
        vorname_form = form.cleaned_data.get('vorname_form')


        nachname_form = form.cleaned_data.get('nachname_form')
        alter_form = form.cleaned_data.get('alter_form')
        email_form = form.cleaned_data.get('email_form')
        print(self.meine_leere_liste)
        mein_ergebnis = self.meine_leere_liste['mein_ergebnis']
        mein_zweites_ergebnis = self.meine_leere_liste['mein_zweites_ergebnis']

        teilnahme_objekte = Teilnahme.objects.create(vorname=vorname_form,
                                                    nachname=nachname_form,
                                                    alter=alter_form,
                                                    email=email_form,
                                                    ergebnis_1=mein_ergebnis,
                                                    ergebnis_2=mein_zweites_ergebnis)


        return HttpResponseRedirect(self.get_success_url(form_name))
