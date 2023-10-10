from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'place',
                    'get_poster', 'is_past', 'is_draft')
    list_filter = ('category',)
    search_fields = ('title', 'category__name')
    inlines = [CommentInline, ]
    save_on_top = True
    save_as = True
    list_editable = ('is_past', 'is_draft')
    readonly_fields = ('get_poster',)
    fieldsets = (
        ("Название и категория", {
            "fields": (('title', 'category'), )
        }),
        ("Описание и постер", {
            "fields": (('descrtption', ), ('poster', 'get_poster',), )
        }),
        ("Артисты и организаторы", {
            "fields": (('artists', 'organizer'), )
        }),
        ("Место проведения и дата", {
            "fields": (('place', 'event_date'), )
        }),
        ("У кого в избарнных", {
            "fields": ('favourite', )
        }),
        ("Прошедшее, черновик", {
            "fields": (('is_past', 'is_draft'), )
        }),
    )

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" heigth="60">')

    get_poster.short_description = "Постер"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'event',)
    readonly_fields = ('name', 'email')


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'name', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" heigth="60">')

    get_image.short_description = "Изображение"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'address',)

admin.site.site_tittle = "Бэкенд афишы"
admin.site.site_header = "Бэкенд афишы"