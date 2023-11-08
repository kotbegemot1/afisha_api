from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

from .models import Event, Artist
from .serializers import (
    EventListSerializer, 
    EventDetailSerializer, 
    CommentCreateSerializer, 
    ArtistListSerializer,
    ArtistDetailSerializer
    )
from .service import EventFilter


class EventListView(generics.ListAPIView):
    queryset = Event.objects.filter(is_draft=False)
    serializer_class = EventListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventFilter

class EventDetailView(generics.ListAPIView):
    queryset = Event.objects.filter(is_draft=False)
    serializer_class = EventDetailSerializer

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer

class ArtistListView(generics.ListAPIView):
    """Вывод списка артистов и организаторов"""
    queryset = Artist.objects.all()
    serializer_class = ArtistListSerializer

class ArtistDetailView(generics.RetrieveAPIView):
    """Вывод списка артистов и организаторов"""
    queryset = Artist.objects.all()
    serializer_class = ArtistListSerializer