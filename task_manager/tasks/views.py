from django.shortcuts import render, redirect
from django.views import View
from django.utils.translation import gettext_lazy
from .models import Task
from ..users.models import User
from .forms import TaskForm

TASK_CREATED = gettext_lazy('Задача успешно создана')
TASK_UPDATED = gettext_lazy('Задача успешно изменена')

class TasksView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'tasks/tasks.html', {'tasks': tasks})
    

class TasksCreateView(View):

    def get(self, request, *args, **kwargs):
        form = TaskForm(initial={'author': request.session.get('user_id')})
        return render(request, 'tasks/t_create.html', {'form': form, 'btn': gettext_lazy('Создать')})
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            # author_id = request.session.get('user_id')
            # author = User.objects.get(id=author_id)
            form.save()
            return redirect('/tasks/')
        # save_task(request.POST)
        return render(request, 'tasks/t_create.html', {'form': form, 'btn': gettext_lazy('Создать')})


class TasksUpdateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/tasks.html', {'btn': gettext_lazy('Сохранить')})
    
    def post(self, request, *args, **kwargs):
        return redirect('/tasks/')


class TasksDeleteView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/tasks.html')
    
    def post(self, request, *args, **kwargs):
        return redirect('/tasks/')


def save_task(data, id=0):
    if id > 0:
        t = Task.objects.get(id=id)
    else:
        t = Task()
    t.name = data.get('name')
    t.description = data.get('description')
    t.status = data.get('status')
    t.author = data.get('author')
    t.executor = data.get('executor')
    t.save()
