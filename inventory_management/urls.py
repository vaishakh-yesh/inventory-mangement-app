from django.urls import path
from inventory.views import item_list, add_item, update_item, delete_item

urlpatterns = [
    path('', item_list, name='item_list'),
    path('add/', add_item, name='add_item'),
    path('update/<int:pk>/', update_item, name='update_item'),
    path('delete/<int:pk>/', delete_item, name='delete_item'),
]
