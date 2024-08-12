from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mailings/', RedirectView.as_view(url='mailings/mailings/', permanent=False)),
    path('mailings/mailings/', include('mailings.urls')),
    path('users/', include('users.urls')),
]
