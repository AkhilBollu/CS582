from django.urls import path
from .views import (
    vehicle_create_view, 
    vehicle_detail_view, 
    vehicle_delete_view,
    vehicle_list_view,
    vehicle_update_view,
    
)

app_name = 'vehicles'
urlpatterns = [
    path('', vehicle_list_view, name='vehicle-list'),
    path('create/', vehicle_create_view, name='vehicle-list'),
    path('<int:id>/', vehicle_detail_view, name='vehicle-detail'),
    path('<int:id>/update/', vehicle_update_view, name='vehicle-update'),
    path('<int:id>/delete/', vehicle_delete_view, name='vehicle-delete'),
]