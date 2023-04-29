from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, ChoiceDropdownFilter, DropdownFilter

from .models import ModelTipper, Tipper


@admin.register(ModelTipper)
class ModelTipperAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ("name", "max_load_capacity")


@admin.register(Tipper)
class TipperAdmin(admin.ModelAdmin):
    autocomplete_fields = ["model"]
    list_display = ("id", "model", "max_load_capacity", "current_load_capacity", "overload_capacity")
    list_filter = [('model', RelatedDropdownFilter), ]

    def max_load_capacity(self, obj):
        return obj.model.max_load_capacity

    max_load_capacity.short_description = ModelTipper._meta.get_field("max_load_capacity").verbose_name
