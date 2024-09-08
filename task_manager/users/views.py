from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm
from .models import User
from django.utils.translation import gettext_lazy
import re

ERR_DIFFERENT_PASS = gettext_lazy('Введенные пароли не совпадают.')
ERR_SHORT_PASS = gettext_lazy('Пароль слишком короткий.')
BTN_CREATE = gettext_lazy('Зарегистрировать')
BTN_UPDATE = gettext_lazy('Сохранить')

# def index(request):
#     return render(request, 'User.html')

class UserView(View):

    def get(self, request, *args, **kwargs):
        u = User.objects.all().order_by('created_at')
        return render(request, 'users.html', {'users': u})
    

class UserCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'u_create.html', {'user': request.POST or None, 'btn': BTN_CREATE})
    
    def post(self, request, *args, **kwargs):
        # form = UserForm(request.POST)
        # if form.is_valid():
        #     errors = user_errors(request.POST)
        #     if not errors:
        #         form.save()
        #         return redirect('/users/')
        #     return render(request, 'u_create.html', {'form': form, 'errors': errors})
        errors = user_errors(request.POST)
        if errors:
            return render(request, 'u_create.html', {'user': request.POST, 'errors': errors, 'btn': BTN_CREATE})
        save_data(request.POST)
        return redirect('/login/')
    

class UserUpdateView(View):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        user = User.objects.get(id=id)
        return render(request, 'u_create.html', {'user': user, 'btn': BTN_UPDATE})
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        errors = user_errors(request.POST)
        if errors:
            return render(request, 'u_create.html', {'user': request.POST, 'errors': errors, 'btn': BTN_UPDATE})
        save_data(request.POST, id)
        return redirect('/users/')
    

class UserDeleteView(View):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        user = User.objects.get(id=id)
        return render(request, 'user_delete.html', {'user': user})
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        user = User.objects.get(id=id)
        user.delete()
        return redirect('/users/')


def user_errors(data):
    errors = []
    pas = data.get('password1', '')
    pas2 = data.get('password2', '')
    username = data.get('username', '')
    if len(username) > 150:
        errors.append('too_long_name')
    inv_chars = re.search('[^\w@\.\+-]', username)
    if inv_chars:
        errors.append('invalid_chars')
    if len(pas) < 3:
        errors.append('too_short_pass')
    if pas != pas2:
        errors.append('different_passes')
    return errors


def save_data(data, id=0):
    if id > 0:
        u = User.objects.get(id=id)
    else:
        u = User()
    u.first_name = data.get('first_name')
    u.last_name = data.get('last_name')
    u.username = data.get('username')
    u.password = data.get('password1')
    u.save()
