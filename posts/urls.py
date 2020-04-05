from django.urls import path, include
from .views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='create'),
    path('<int:pk>/', post_detail, name='detail'),
    path('<int:pk>/edit/', post_update, name='update'),
    path('<int:pk>/delete/', post_delete, name='delete'),
]