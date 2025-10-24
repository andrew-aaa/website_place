from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.html import format_html


class PlaceImageInline(admin.TabularInline):
    """
    Inline-админка для отображения и редактирования изображений места непосредственно в форме редактирования места
        
    Attributes:
        model: Модель PlaceImage для inline отображения
        extra: Количество дополнительных пустых форм для добавления изображений
        fields: Поля, отображаемые в inline форме
        readonly_fields: Поля, доступные только для чтения
    """

    model = PlaceImage
    extra = 1   
    fields = ('image', 'position', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        """
        Генерирует HTML для предпросмотра изображения
            
        @param {PlaceImage} obj - Объект изображения места
        @return {str} - HTML код для отображения изображения или текст "Нет изображения"
        """

        if obj.image:
            return format_html(
                '<img src="{}" height="100" />',
                obj.image.url
            )
        return "Нет изображения"
    image_preview.short_description = 'Предпросмотр'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    """
    Админка для модели Place - управления местами на карте
        
    Attributes:
        list_display: Поля, отображаемые в списке объектов
        list_filter: Поля для фильтрации списка объектов  
        search_fields: Поля, по которым осуществляется поиск
        inlines: Inline-админки для связанных объектов
    """

    list_display = ('title', 'lng', 'lat')
    list_filter = ('title',)
    search_fields = ('title',)
    inlines = [PlaceImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    """
    Админка для модели PlaceImage - управления изображениями мест
        
    Attributes:
        list_display: Поля, отображаемые в списке изображений
        list_filter: Поля для фильтрации списка изображений
        readonly_fields: Поля, доступные только для чтения в форме редактирования
    """

    list_display = ('place', 'position', 'image_preview')
    list_filter = ('place',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        """
        Генерирует HTML для предпросмотра изображения в списке объектов
        
        @param {PlaceImage} obj - Объект изображения места
        @return {str} - HTML код для отображения изображения или текст "Нет изображения"
        """

        if obj.image:
            return format_html(
                '<img src="{}" height="100" />',
                obj.image.url
            )
        return "Нет изображения"
    image_preview.short_description = 'Предпросмотр'