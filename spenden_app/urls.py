from django.urls import path
from .views import TeilnahmeCreate, co2_berechnen, unser_erster_ajax_call

app_name = 'spenden_app'

urlpatterns = [
    path('spenden/', TeilnahmeCreate.as_view(), name='spenden_page'),
    path('CO2/Berechnen/', co2_berechnen, name='calcute_co2_footprint'),
    path('ajax/result/', unser_erster_ajax_call, name='mein_ajax_call'),  # <-- this one here
    # path('spenden/neu/', MultipleFormsDemoView.as_view(), name='spenden_page_neu'),
    # path('teilname/', TeilnameView.as_view(), name='spenden_page'),
    # path('teilname/', views.teilnameview, name='teilname_page'),
# path('', HomeView.as_view(), name='home_page'),
]
