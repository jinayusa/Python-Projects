from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('api_data/', views.api_data_visualization, name='api_data_visualization'),
]
