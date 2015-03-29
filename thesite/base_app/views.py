from django.shortcuts import render
import communication_app.models
import django.contrib.auth.views


def logout(request):
    return django.contrib.auth.views.logout(
        request,
        next_page='/',
    )


def site_index(request):
    recent_updates = communication_app.models.Update.objects.all()
    return render(
        request,
        'base_app/site_index.html', {
            'recent_updates': recent_updates,
        }
    )
