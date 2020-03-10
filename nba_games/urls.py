from django.urls import path, include
from .views import GamesView

urlpatterns = [
    path('games/', GamesView.as_view(), name='games'),
]