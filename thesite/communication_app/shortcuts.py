import communication_app.models


def get_my_pets(request):
    if not request.user:
        return []
    return communication_app.models.Pet.objects.filter(user=request.user)
