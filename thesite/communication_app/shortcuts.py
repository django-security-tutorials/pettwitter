from .models import Pet


def get_my_pets(request):
    # If this is an anonymous user, they don't have any pets.
    if not request.user.is_authenticated:
        return []
    return Pet.objects.filter(user=request.user)
