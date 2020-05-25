from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'about_app'

urlpatterns = [
    path('about/', views.aboutview, name='about_page'),

]
