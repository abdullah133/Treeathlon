from django.urls import path

from . import views
from django.conf.urls import url

app_name = 'contact_app'

urlpatterns = [
    path('contact/', views.contactview, name='contact_page'),
    path('contact/success', views.contactgeschafftview, name='contact_success_page'),

]
