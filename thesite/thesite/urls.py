from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # For everything generic, look in base_app
    path("", include("base_app.urls")),
    # For pet communication views, prefix with pets. This contains the bulk of this
    # project's application logic.
    path('pets/', include('communication_app.urls', namespace='pets')),
    # Include the views from Asheesh's Django Optimizer
    # TODO: Update asheeshs_django_optimizer for modern Django
    # path('optimizer/', include('asheeshs_django_optimizer.urls')),
    # Django admin.
    path('admin/', admin.site.urls),
]
