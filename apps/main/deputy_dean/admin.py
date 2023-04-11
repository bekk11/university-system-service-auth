from django.contrib import admin

from apps.main.deputy_dean.models import DeputyDean


@admin.register(DeputyDean)
class DeputyDeanAdmin(admin.ModelAdmin):
    list_display = ["user", "dean", "fullname", "gender"]
    list_filter = ["gender", "dean"]
    list_display_links = ["user", "dean", "fullname"]
    search_fields = ["user", "dean"]
    ordering = ["-id"]
