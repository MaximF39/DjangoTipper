import public_admin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, ChoiceDropdownFilter, DropdownFilter
from public_admin.sites import PublicApp, PublicAdminSite

from .models import ModelTipper, Tipper

User = get_user_model()

public_app = PublicApp("logistic", models=("Tipper",))
public_admin = PublicAdminSite("dashboard", public_app)


@admin.register(ModelTipper)
class ModelTipperAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ("name", "max_load_capacity")


class TipperPublicAdmin(admin.ModelAdmin):
    list_display = ("id", "model", "max_load_capacity", "current_load_capacity", "overload_capacity")
    list_filter = [('model', RelatedDropdownFilter), ]

    def max_load_capacity(self, obj):
        return obj.model.max_load_capacity

    max_load_capacity.short_description = ModelTipper._meta.get_field("max_load_capacity").verbose_name


@admin.register(Tipper)
class TipperAdmin(TipperPublicAdmin):
    autocomplete_fields = ["model"]


public_admin.register(Tipper, TipperPublicAdmin)
