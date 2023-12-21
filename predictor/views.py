from django.shortcuts import render
from .forms import 

def predict_seat(request):
    if request.method == 'POST':
        form = PredictionForm
