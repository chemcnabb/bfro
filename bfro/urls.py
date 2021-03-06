# coding: utf-8
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls import patterns, include, url

from django.conf.urls.static import static
from django.contrib import admin
from bfro.apps.sighting.views import MapView, sightings_view

# Added to allow for robots.txt at root
from django.http import HttpResponse




urlpatterns = patterns(
   url(r'^i18n/', include('django.conf.urls.i18n')),
   url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^timeline/', include('timelinejs.urls')),
    url(r'^sightings/', sightings_view, name='sightings'),
   url(r'^admin/', include(admin.site.urls)),
   # Adding url for robots.txt
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),


    #url(r'^search/$', SearchView.as_view(), name='search'),

    url(r'^home/$', MapView.as_view(), name='home'),
    url(r'^$', RedirectView.as_view(url='/home/', permanent=True)),

)

urlpatterns += patterns("",
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
)
