from django.urls import path
from . import views

urlpatterns = [
    path('places.geojson', views.places_geojson, name='places_geojson'),                        # Маршрут для получения GeoJSON со всеми местами
    path('places/<int:place_id>/json/', views.place_detail_json, name='place_detail_json'),     # Маршрут для получения детальной информации о конкретном месте
]