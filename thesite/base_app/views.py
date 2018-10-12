from django.contrib.auth import authenticate
from django.contrib.auth import login as django_auth_login
from django.contrib.auth import logout as django_auth_logout
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render

from communication_app.models import Update


def logout(request):
    django_auth_logout(request)
    return HttpResponseRedirect("/")


def site_index(request):
    recent_updates = Update.objects.all().order_by("-pub_date")
    return render(
        request, "base_app/site_index.html", {"recent_updates": recent_updates}
    )


def login(request):
    # We allow people to log in.
    #
    # For the purposes of security auditing, ignore any bugs in this
    # function.
    #
    #
    # Yes, that means you, dear people attending the tutorial!
    #
    # The rest of the app has so many bugs that really I don't want to
    # hear about bugs you find in this particular view.
    #
    # If you want to steal someone else's account, don't do it via
    # the login view.

    # Get the login credentials that were submitted, and check if they
    # are valid.
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)

    # If so, great! Log them in.
    if user is not None:
        if user.is_active:
            django_auth_login(request, user)

    # Either way, redirect back to the homepage.
    return HttpResponseRedirect("/")


def create_user(request):
    # We allow anyone to create a username.
    #
    # For the purposes of security auditing, ignore any bugs in this
    # function.
    #
    # Yes, that means you, dear people attending the tutorial!
    #
    # The rest of the app has so many bugs that really I don't want to
    # hear about bugs you find in this particular view.

    # Make sure the user is not logged in while creating a new user; that would just be
    # weird.
    if request.user.is_authenticated:
        raise PermissionDenied

    # Make sure no user exists with the desired username.
    desired_username = request.POST["username"].lower().strip()
    if User.objects.filter(username=desired_username):
        raise PermissionDenied

    # OK, then let's create one.
    User.objects.create_user(
        desired_username, email=None, password=request.POST["password"]
    )

    user = authenticate(username=desired_username, password=request.POST["password"])

    if user is not None:
        if user.is_active:
            django_auth_login(request, user)

    # Let's just redirect to the front page.
    return HttpResponseRedirect("/")
