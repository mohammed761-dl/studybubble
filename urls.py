from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),    # core app URLs (home, login, signup)
    path('groups/', include('groups.urls')),  # groups app URLs
]

