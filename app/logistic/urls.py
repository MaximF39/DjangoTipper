from django.urls import path

from .admin import public_admin

urlpatterns = [
    path("view/", public_admin.urls)
]
