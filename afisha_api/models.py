from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    """Категория событыя"""
    name = models.CharField("Категория", max_length=100)
    description = models.TextField("Описание")
    # url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Artist(models.Model):
    """Артисты и организаторы"""
    nickname = models.CharField("Псавдоним", max_length=100)
    name = models.CharField("Имя", max_length=100)
    image = models.ImageField("Изображение", upload_to="artists/")
    
    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Артисты и организаторы'
        verbose_name_plural = 'Артисты и организаторы'

class Place(models.Model):
    """Место проведения мероприятия"""
    title = models.CharField("Место", max_length=100)
    descrtption = models.TextField("Описание")
    address = models.CharField("Адрес", max_length=100)

    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Адрес проведения'
        verbose_name_plural = 'Адрес проведения'

class Event(models.Model):
    """События"""
    title = models.CharField("Название",max_length=100)
    descrtption = models.TextField("Описание")
    artists = models.ManyToManyField(Artist, verbose_name="Участники", related_name="event_artist")
    organizer = models.ManyToManyField(Artist, verbose_name="Организаторы", related_name="event_organizer")
    place = models.ForeignKey(Place, related_name='event_place', verbose_name="Место проведения", on_delete=models.SET_NULL, null=True)
    poster = models.ImageField("Постер", upload_to="events/")
    category = models.ForeignKey(Category, related_name="event_category", verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    event_date = models.DateTimeField("Время проведения")
    favourite = models.ManyToManyField(User, verbose_name="Избранное", related_name="event_favourite", blank=True)
    is_past = models.BooleanField("Прошедшее событие", default=False)
    is_draft = models.BooleanField("Черновик", default=False)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

class Comment(models.Model):
    """Комментарии"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey("self", verbose_name="Родитель", related_name="children", on_delete=models.SET_NULL, blank=True, null=True)
    event = models.ForeignKey(Event, verbose_name="Событие", related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.event}"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
