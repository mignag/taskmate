from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import TaskList
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required     #aplicar a view/função seguinte apenas a utilizadores autenticados
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
        messages.success(request,("New task added successfully!"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(owner=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})
    
    #context = {
    #    'welcome_text':"Welcome to to-do list app."
    #}
    #return render(request, 'todolist.html', context)
    # return render(request, 'todolist.html', {})
    # return HttpResponse("Welcome to to-do list...")

@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance= task)
        if form.is_valid():
            form.save()
        messages.success(request,("task edited!"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        if task.done == True:
            task.done = False
        else:
            task.done = True
        task.save()
    else:
        messages.error(request,("restricted access operation!"))
    return redirect('todolist')

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request,("restricted access operation (only owners can delete...)"))
    return redirect('todolist')

def index(request):
    context = {
        'index_text':"Welcome to index page."
    }
    return render(request, 'index.html', context)

def contact(request):
    context = {
        'welcome_text':"Welcome to contact page."
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'welcome_text':"Welcome to about page."
    }
    return render(request, 'about.html', context)

