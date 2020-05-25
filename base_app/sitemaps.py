
from django.urls import reverse
from django.contrib import sitemaps


class StaticViewSitemap(sitemaps.Sitemap):

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home_page',]

    def location(self, item):
        return reverse(item)
