# Django
from django.contrib import admin

# Project
from apps.main.dean.models import Dean


@admin.register(Dean)
class DeanAdmin(admin.ModelAdmin):
    """
    This admin class is used to customize the DEAN admin panel.
    """
    # Admin can filter by DEAN gender - 18 line.
    # Admin can enter to one DEAN by user, fullname - 19 line.
    # Admin can search by DEAN user - 20 line.
    list_display = ["user", "fullname", "gender"]
    list_filter = ["gender"]
    list_display_links = ["user", "fullname"]
    search_fields = ["user"]
    ordering = ["-id"]
