from django.shortcuts import render, redirect
from .models import MyModel

def create_my_model(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        MyModel.objects.create(name=name)
        return redirect('my_model_list') 
    return render(request, 'create_my_model.html', {})

def my_model_list(request):
    my_models = MyModel.objects.all()
    return render(request, 'my_model_list.html', {'my_models': my_models})

# You can add more views as needed for testing and display
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
