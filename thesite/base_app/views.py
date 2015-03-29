from django.shortcuts import render
import communication_app.models


def site_index(request):
    recent_updates = communication_app.models.Update.objects.all()
    return render(
        request,
        'base_app/site_index.html', {
            'recent_updates': recent_updates,
        }
    )
