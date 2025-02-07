from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('create_model/', views.create_model, name='create_model'),  # Example URL pattern
]