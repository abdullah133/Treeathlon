from django.shortcuts import render
from .models import PartnerInfo, PartnerDescription
from django.views.generic.base import TemplateView
# Create your views here.
class PartnerView(TemplateView):
    template_name = 'partner_app/partner.html'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        mein_header_bild = 'partner-banner-area relative'


        partner_info = PartnerInfo.objects.all()
        partner_discriptions = PartnerDescription.objects.all()

        context = {
                    'partner_info':partner_info,
                    'partner_discriptions':partner_discriptions,
                    'mein_header_bild':mein_header_bild,
                                        }
        return context
