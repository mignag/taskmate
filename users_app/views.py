from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
#deixa de importar o form standar pq vai usar o custom (que herda deste...)
#from django.contrib.auth.forms import UserCreationForm
#from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method=="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("new user account created, login to get started!"))
            return redirect('register')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})
    # return HttpResponse("users_app working")