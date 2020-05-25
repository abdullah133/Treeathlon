from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'privacy_app'

urlpatterns = [
    path('privacy/', views.privacyview, name='privacy_page'),

]
