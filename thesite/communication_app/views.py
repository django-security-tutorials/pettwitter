from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

import communication_app.forms
import communication_app.shortcuts


def site_index(request):
    return render(request, 'site_index.html')


def index(request):
    my_pets = communication_app.shortcuts.get_my_pets(request)
    pet_form = communication_app.forms.PetForm()
    return render(
        request,
        'communication_app/index.html', {
            'my_pets': my_pets,
            'pet_form': pet_form,
        }
    )


def new_pet(request):
    # If user is not logged in, return HTTP 403.
    if not request.user.is_authenticated:
        return HttpResponse(status=403)

    # Since the user _is_ logged in, we validate the
    # form data.

    form = communication_app.forms.PetForm(
        request.GET or request.POST)
    if form.is_valid():
        # The validated data is in the form instance. Calling
        # form.save() will result in the creation of a Django ORM
        # instance that has the data from the form pre-loaded.
        #
        # We pass commit=False so that we get a Django ORM instance
        # where it hasn't been saved to the database yet.
        new_pet = form.save(commit=False)

        # Scrupulously copy the currently logged in user into the
        # object -- the user is a required field in the model, and we
        # don't trust the user submitting the data to give us their
        # user ID.
        new_pet.user = request.user

        # Now actually save it to the database.
        new_pet.save()
    else:
        # If this were a real app, we might do something like show the
        # user the form data they submitted or show them what is wrong
        # with their input. Since it is just a demo, we err on the
        # side of simplicity and redirect back to the index.
        #
        # Since we do that no matter what at the end of this view,
        # we can just do nothing in the else case.
        pass

    # Finally, take the user back to their pet index.
    return HttpResponseRedirect(reverse(index))


def profile(request, pet_id):
    # All pet data is public in the systemm, so this view
    # doesn't do any access control.
    pet = get_object_or_404(communication_app.models.Pet, pk=pet_id)
    update_form = communication_app.forms.UpdateForm()
    return render(
        request,
        'communication_app/profile.html', {
            'pet': pet,
            'update_form': update_form,
        }
    )


def update(request, pet_id):
    # Here we accept an update from the user and make a new Update
    # object, making sure the user owns the pet in question.

    # If the user is not logged in, reject the request.
    if not request.user.is_authenticated():
        return HttpResponse(status=403)

    # If they're trying to update a non-existent pet, reject the
    # request with a 404.
    pet = get_object_or_404(communication_app.models.Pet, pk=pet_id)

    # If the user is trying to update a pet they don't own,
    # reject the request.
    if pet.user != request.user:
        return HttpResponse(status=403)

    # Now take the data in the POST and store in the database;
    # after that's done, we'll redirect the user back to this
    # pet's profile page, so that they can see the update.
    #
    # Since this app is pretty simple, if the form is somehow
    # invalid, we don't bother sending the user any information
    # about how it's invalid.
    form = communication_app.forms.UpdateForm(
        request.POST)
    if form.is_valid():
        # The logic here is very similar to the new_pet() view.
        update_instance = form.save(commit=False)
        update_instance.pet = pet
        update_instance.save()

    # Now send the person back to the pet index page.
    return HttpResponseRedirect(reverse(profile,
                                        args=(pet_id,)))


def set_description(request, pet_id):
    # Here we let the user set a description for a pet of theirs.

    # If the user is not logged in, reject the request.
    if not request.user.is_authenticated():
        return HttpResponse(status=403)

    # If they're trying to update a non-existent pet, reject the
    # request with a 404.
    pet = get_object_or_404(communication_app.models.Pet, pk=pet_id)

    # If the user is trying to describe a pet they don't own, reject
    # the request.
    if pet.user != request.user:
        return HttpResponse(status=403)

    # If they gave us no description, reject.
    raw_user_provided_description =  request.POST.get('description', None)
    if raw_user_provided_description is None:
        return HttpResponse(status=403)

    # Slice it to just be 1024 characters, since that's the length in
    # the database.
    raw_user_provided_description = raw_user_provided_description[:1024]

    # If the incoming description is not valid UTF-8, then reject the
    # request.
    try:
        user_provided_description = unicode(raw_user_provided_description)
    except UnicodeDecodeError:
        return HttpResponse(status=403)

    # Seems good. Let's store it.
    pet.description = user_provided_description
    pet.save()

    # Redirect them back to the profile for this pet.
    return HttpResponseRedirect('/pets/profiles/%d' % (
        pet.id,))
