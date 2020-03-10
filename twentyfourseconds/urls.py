from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('users/', include('users.urls')),
    path('', include('nba_games.urls')),
]
