from django.urls import path
from .views import ClientListAPIView,ClientDetailAPIView,ProjectListAPIView,ProjectDetailAPIView

urlpatterns = [
    path('clients/', ClientListAPIView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailAPIView.as_view(), name='client-detail'),
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
]
