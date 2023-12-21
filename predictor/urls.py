from django.urls import path
from .views import predict_seat

urlpatterns = [
    path('predict/', predict_seat, name = 'predict_seat')
]