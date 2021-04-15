from django.urls import path
from . import views


urlpatterns = [
    path ("", views.contact, name = "Contact"),
    path ("snippet", views.snippet_detail, name = "Snippet"),
]