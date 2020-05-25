from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'events_app'

urlpatterns = [
    path('events/', views.eventsview, name='events_page'),

]
