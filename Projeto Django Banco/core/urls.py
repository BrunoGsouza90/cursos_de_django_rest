from django.contrib import admin
from django.urls import path
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    # Está URL redirecionará para os ROUTERs do Django Ninja.
    path('api/', api.urls)
]
