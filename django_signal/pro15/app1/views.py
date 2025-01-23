from django.shortcuts import render
from .models import MyModel
import threading
from django.shortcuts import render

def create_model(request):
    print(f"Creating model in thread: {threading.current_thread().name}")
    MyModel.objects.create(name="Test")
    return render(request, 'success.html')


# def create_model(request):
    # ... (your existing create_model view code) ...

def home(request):
    return render(request, 'home.html')