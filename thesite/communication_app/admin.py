from django.contrib import admin

from .models import Pet, Update


class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    list_select_related = True


class UpdateAdmin(admin.ModelAdmin):
    list_display = ("__str__", "pet")
    list_select_related = True


admin.site.register(Pet, PetAdmin)
admin.site.register(Update, UpdateAdmin)
