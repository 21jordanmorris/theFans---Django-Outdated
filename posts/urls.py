from django.urls import path, include
from .views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='create'),
    path('<slug>/', post_detail, name='detail'),
    path('<slug>/edit/', post_update, name='update'),
    path('<slug>/delete/', post_delete, name='delete'),
]