from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("mailings/", include("mailings.urls")),
    path("users/", include("users.urls")),
    path('', blog_views.home, name='home'),
]
