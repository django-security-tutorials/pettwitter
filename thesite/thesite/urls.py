from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render


urlpatterns = patterns(
    '',  # First arg to patterns is a namespace parameter.

    # A couple of views in a base app.
    url(r'^$', 'base_app.views.site_index'),
    url(r'^logout/$', 'base_app.views.logout'),

    # Actual pet communication views -- most of the app is here.
    url(r'^pets/', include('communication_app.urls')),

    # Django admin.
    url(r'^admin/', include(admin.site.urls)),
)
