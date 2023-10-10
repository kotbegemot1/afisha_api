from django.urls import  path

from . import views

urlpatterns = [
    path('events/', views.EventListView.as_view()),
    path('events/<int:pk>/', views.EventDetailView.as_view()),
    path('comments/', views.CommentCreateView.as_view()),
    path('artists/', views.ArtistListView.as_view()),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view()),
]