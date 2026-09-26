"""
URL configuration for chatbot_project.

The chat bot is used from the terminal (``python manage.py chat``), so the
only URL exposed is Django's admin, where the trained statements can be
browsed under "Django ChatterBot".
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
