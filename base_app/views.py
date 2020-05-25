from django.shortcuts import render
from django.views.generic import View, FormView
from about_app.models import Team
from .forms import JoinForm
from .models import Join, BeschreibungenHomeSeite, Vision, TreeathlonInZahlen, BackgroundImgDescription
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from spenden_app.models import Teilnahme
# Create your views here.
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from partner_app.models import PartnerInfo


class HomeView(TemplateView):
    template_name = 'base_app/home.html'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        meinebeschreibungen = BeschreibungenHomeSeite.objects.all()[:3]
        anzahl_teilnehmer = Teilnahme.objects.all().count()
        anzahl_team_mitglieder = Team.objects.all().count()
        anzahl_team_partner = PartnerInfo.objects.all().count()
        unser_vision = Vision.objects.all()
        treeathlon_zahlen = TreeathlonInZahlen.objects.all()
        background_cotnent = BackgroundImgDescription.objects.all()

        context = {'anzahl_teilnehmer':anzahl_teilnehmer,
                    'meinebeschreibungen':meinebeschreibungen,
                    'anzahl_team_mitglieder':anzahl_team_mitglieder,
                    'unser_vision':unser_vision,
                    'treeathlon_zahlen':treeathlon_zahlen,
                    'background_cotnent':background_cotnent,
                    'homesite':True,
                    'anzahl_team_partner':anzahl_team_partner

                                        }
        return context




def newsletter_view(request):
    if request.method == 'POST':
        print('i han en post')
        newsletterform = JoinForm(data=request.POST)
        if newsletterform.is_valid():
            neue_email_adresse = newsletterform.cleaned_data['email']
            vorh_email_adressen = Join.objects.filter(email = newsletterform.cleaned_data['email']).count()
            print('vorh_email_adressen:'+str(vorh_email_adressen))
            if vorh_email_adressen == 0:
                newsletterform.save()
            else:
                print('diese Email Adresse ist bereits vorhanden')


        next = request.POST.get('next',None)
        if next:
            print(next)
            return redirect(next) # you can include some query strings as well
        else :
            print('lkhlkjlkjlkjljljlj')
            return reverse_lazy('base_app:home_page')

    else:
        print('es isch getttttttttttt')
        newsletterform = JoinForm()
