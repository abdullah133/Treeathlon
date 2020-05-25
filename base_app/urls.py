from django.urls import path
from.views import HomeView,newsletter_view
from django.conf.urls import url
from .sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static': StaticViewSitemap,
}


app_name = 'base_app'

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('newsletter/', newsletter_view, name='newsletter_page'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap')


]
