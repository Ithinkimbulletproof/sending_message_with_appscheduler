from django.urls import path
from . import views

urlpatterns = [
    path("", views.mailing_list, name="mailing_list"),
    path("<int:pk>/", views.mailing_detail, name="mailing_detail"),
    path("create/", views.mailing_create, name="mailing_create"),
    path("<int:pk>/edit/", views.mailing_edit, name="mailing_edit"),
    path("<int:pk>/delete/", views.mailing_delete, name="mailing_delete"),
]
