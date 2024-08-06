from django.urls import path

from .views import item_detail, item_list, item_list_serialized

urlpatterns = [
    path('', item_list, name='home'),
    path('drf/', item_list_serialized, name='drf'),
    path('<int:pk>/', item_detail, name='item-detail'),
]
