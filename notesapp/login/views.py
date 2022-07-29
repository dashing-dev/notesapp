from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import is_valid_path
   

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save 
    
    context = {'form':form}

    return render(request, 'register.html' , context)



def login(request):
    return HttpResponse('this is login page')