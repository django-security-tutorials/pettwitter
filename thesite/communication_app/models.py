from django.db import models
from django.contrib import admin


class Pet(models.Model):
    pass


class Update(models.Model):
    pub_date = models.DateTimeField(
        # Use current time on obj creation.
        auto_now_add=True,
    )
    pet = models.ForeignKey(Pet)

admin.site.register(Update)
admin.site.register(Pet)
