from django.db import models


class Place(models.Model):
    """
    Модель для представления места на карте
    
    Attributes:
        title (CharField): Название места
        description_short (TextField): Краткое описание места
        description_long (TextField): Полное описание места с HTML разметкой
        lng (FloatField): Долгота географических координат
        lat (FloatField): Широта географических координат
    """

    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        """
        Строковое представление объекта Place
        
        @return {str} - Название места
        """

        return self.title
    
    class Meta:
        """
        Метаданные модели Place
        
        Attributes:
            verbose_name: Человекочитаемое название в единственном числе
            verbose_name_plural: Человекочитаемое название во множественном числе
        """

        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlaceImage(models.Model):
    """
    Модель для представления изображений, связанных с местом
    
    Attributes:
        place (ForeignKey): Связь с местом, к которому относится изображение
        image (ImageField): Файл изображения
        position (PositiveIntegerField): Позиция изображения для сортировки
    """

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )
    image = models.ImageField('Изображение', upload_to='places/')
    position = models.PositiveIntegerField('Позиция', default=0)

    class Meta:
        """
        Метаданные модели PlaceImage
        
        Attributes:
            ordering: Порядок сортировки объектов по умолчанию
            verbose_name: Человекочитаемое название в единственном числе
            verbose_name_plural: Человекочитаемое название во множественном числе
        """
        
        ordering = ['position']
        verbose_name = 'Изображение места'
        verbose_name_plural = 'Изображения мест'
    
    def __str__(self):
        """
        Строковое представление объекта PlaceImage
        
        @return {str} - Строка в формате "позиция - название места"
        """
        
        return f'{self.position} - {self.place.title}'