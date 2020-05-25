from django.urls import path
from . import views
from django.conf.urls import url
from .views import PartnerView

app_name = 'partner_app'

urlpatterns = [
    path('partner/', PartnerView.as_view(), name='partner_page'),

]
