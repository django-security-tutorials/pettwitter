from django.contrib.auth.admin import UserAdmin


# Override default list_display for the UserAdmin
# Including password in the list of fields displayed should be safe because all that's stored there is a hashed
# value, so no actual user passwords will be exposed
UserAdmin.list_display = (
    "pk",
    "username",
    "password",
    "email",
    "first_name",
    "last_name",
    "is_staff",
)
