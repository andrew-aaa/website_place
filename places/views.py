from django.http import JsonResponse
from .models import Place


def places_geojson(request):
    """
    View-функция для получения всех мест в формате GeoJSON
    Формирует GeoJSON объект со всеми местами из базы данных для отображения на карте
    
    @param request (HttpRequest) - Объект HTTP запроса
    @return {JsonResponse} - GeoJSON объект с данными всех мест
    """

    places = Place.objects.all()
    
    features = []
    for place in places:
        # Создаем GeoJSON feature для текущего места
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]   
            },
            'properties': {
                'title': place.title,
                'placeId': f'place_{place.id}',
                'detailsUrl': f'/places/{place.id}/json/'
            }
        }
        features.append(feature)

    # Формируем полный GeoJSON объект
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return JsonResponse(geojson, json_dumps_params={'ensure_ascii': False})


def place_detail_json(request, place_id):
    """
    View-функция для получения детальной информации о конкретном месте
    
    Возвращает полную информацию о месте включая изображения и координаты
    
    @param {HttpRequest} request - Объект HTTP запроса
    @param {int} place_id - ID запрашиваемого места    
    @return {JsonResponse} - JSON объект с детальной информацией о месте
    @return {JsonResponse} - JSON с ошибкой 404 если место не найдено
    """

    try:
        place = Place.objects.prefetch_related('images').get(id=place_id)

        # Формируем список абсолютных URL изображений места
        imgs = [request.build_absolute_uri(image.image.url) for image in place.images.all()]

        # Формируем данные для ответа
        data = {
            'title': place.title,
            'imgs': imgs,
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': {
                'lng': f"{place.lng:.14f}",
                'lat': f"{place.lat:.14f}"
            }
        }

        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    except Place.DoesNotExist:
        return JsonResponse({'error': 'Place not found'}, status=404)