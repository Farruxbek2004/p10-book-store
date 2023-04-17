from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name", "is_staff"]
    list_editable = ["first_name", "last_name"]
    list_filter = ["is_staff", "is_superuser", "is_active"]
    list_display_links = ["username", "email"]
    search_fields = ["username", "email", "first_name", "last_name"]
    search_help_text = "Qidirish"


admin.site.register(User, UserAdmin)

# password: farruxbek
# parol: 123
