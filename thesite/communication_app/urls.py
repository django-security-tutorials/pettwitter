from django.urls import path

from . import views

app_name = "pets"
urlpatterns = [
    path("", views.index, name="index"),
    # TODO: Verify paths below this comment
    path("new_pet/", views.new_pet, name="new_pet"),
    path("profiles/<int:pet_id>/", views.profile, name="profile"),
    path("update/<pet_id>/", views.update, name="update"),
    path("set_description/<int:pet_id>", views.set_description, name="set_description"),
    path("delete_my_pets/", views.delete_my_pets, name="delete_my_pets"),
]
