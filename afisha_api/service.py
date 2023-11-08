from django_filters import rest_framework as filters

from .models import Event

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class EventFilter(filters.FilterSet):
    category = CharFilterInFilter(
        field_name='category__name', lookup_expr='in')
    month = filters.CharFilter(field_name='event_date', lookup_expr='month')

    class Meta:
        model = Event
        fields = ['category', 'event_date']
