from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    # For everything generic, look in base_app
    path("", include("base_app.urls"))
]

# urlpatterns = patterns(
#
#     # Actual pet communication views -- most of the app is here.
#     url(r'^pets/', include('communication_app.urls')),
#
#     # Include the views from Asheesh's Django Optimizer
#     url(r'^optimizer/', include('asheeshs_django_optimizer.urls')),
#
#     # Django admin.
#     url(r'^admin/', include(admin.site.urls)),
# )
