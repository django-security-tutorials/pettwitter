from django.contrib.auth.admin import UserAdmin


# Override default list_display for the UserAdmin
UserAdmin.list_display = (
    "pk",
    "username",
    "password",
    "email",
    "first_name",
    "last_name",
    "is_staff",
)
