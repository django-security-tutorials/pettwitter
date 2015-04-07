from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import communication_app.models
import django.contrib.auth
import django.contrib.auth.views


def logout(request):
    return django.contrib.auth.views.logout(
        request,
        next_page='/',
    )


def site_index(request):
    recent_updates = communication_app.models.Update.objects.all().order_by('-pub_date')
    return render(
        request,
        'base_app/site_index.html', {
            'recent_updates': recent_updates,
        }
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
    username = request.POST['username']
    password = request.POST['password']
    user = django.contrib.auth.authenticate(
        username=username,
        password=password,
    )

    # If so, great! Log them in.
    if user is not None:
        if user.is_active:
            django.contrib.auth.login(request, user)

    # Either way, redirect back to the homepage.
    return HttpResponseRedirect('/')


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

    # Make sure the user is not logged while creating a new user; that would just be weird.
    if request.user.is_authenticated():
        return HttpResponse(status=403)

    # Make sure no user exists with the desired username.
    desired_username = request.POST['username'].lower().strip()
    if django.contrib.auth.models.User.objects.filter(
            username=desired_username):
        return HttpResponse(status=403)

    # OK, then let's create one.
    django.contrib.auth.models.User.objects.create_user(
        desired_username,
        email=None,
        password=request.POST['password'],
    )

    user = django.contrib.auth.authenticate(
        username=desired_username,
        password=request.POST['password']
    )

    if user is not None:
        if user.is_active:
            django.contrib.auth.login(request, user)

    # Let's just redirect to the front page.
    return HttpResponseRedirect('/')
