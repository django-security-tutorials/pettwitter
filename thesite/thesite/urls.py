from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render


urlpatterns = patterns(
    '',  # First arg to patterns is a namespace parameter.

    # Just one index view in a base app.
    url(r'^$', 'base_app.views.site_index'),

    # Actual pet communication views -- most of the app is here.
    url(r'^pets/', include('communication_app.urls')),

    # Django admin.
    url(r'^admin/', include(admin.site.urls)),
)
