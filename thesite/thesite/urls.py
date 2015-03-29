from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',  # First arg to patterns is a namespace parameter.

    # Actual pet communication views.
    url(r'^pets/', include('communication_app.urls')),

    # Django admin.
    url(r'^admin/', include(admin.site.urls)),
)
