from django.urls import path, include
from .views import *

urlpatterns = [
    path('', GamesView.as_view(), name='games'),
    path('<int:id>/', game_detail, name='game_detail')
]