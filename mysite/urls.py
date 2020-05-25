from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Treeathlon_Administration"
admin.site.site_title = "Treeathlon"
admin.site.index_title = "Willkommen in Treeathlon Administration Seite"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_app.urls')),
    path('', include('contact_app.urls')),
    path('', include('about_app.urls')),
    path('', include('post_app.urls')),
    path('', include('spenden_app.urls')),
    path('', include('events_app.urls')),
    path('', include('partner_app.urls')),
    path('', include('privacy_app.urls')),

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
