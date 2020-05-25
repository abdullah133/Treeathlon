from django.shortcuts import render, redirect
from .forms import TeilnahmeForm, FrageForm
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView
from .models import Teilnahme, SpendeDescription
from .rechner import berechnung_co2_ausfuehren

from django.views.generic.edit import CreateView

def co2_berechnen(request):

    if request.method == "POST":

        form = FrageForm(request.POST)

        if form.is_valid():
            dict = berechnung_co2_ausfuehren(request, form)
            print('dict:'+str(dict))
        else:
            print('invaaaaaaaaaaaaaaaaaaaaaaaaalid')
            print('error:'+str(form.errors))

        return redirect('spenden_app:spenden_page')


def unser_erster_ajax_call(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'hr/city_dropdown_list_options.html', {'cities': cities})


class TeilnahmeCreate(CreateView):
    model = Teilnahme
    form_class=TeilnahmeForm
    template_name = 'spenden_app/spenden.html'


    def get_context_data(self, **kwargs):
        context = super(TeilnahmeCreate, self).get_context_data(**kwargs)
        mein_header_bild = 'spenden-banner-area'
        spende_description = SpendeDescription.objects.all()
        form = TeilnahmeForm
        context = {'spende_description':spende_description,
        'mein_header_bild':mein_header_bild,
        'frage_form': FrageForm,
        'form':form
}
        return context

    def form_valid(self, form):

        return super(TeilnahmeCreate, self).form_valid(form)
