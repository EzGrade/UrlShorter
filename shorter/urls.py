from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShorterViewSet.as_view({'post': 'create'}), name='shorter-create'),
    path('<str:pk>/', views.ShorterViewSet.as_view({'get': 'retrieve'}), name='shorter-retrieve'),
]
