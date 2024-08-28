from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm
from .models import Users

# def index(request):
#     return render(request, 'users.html')

class UsersView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users.html')
    

class UserCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'u_create.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        if validate_user(**kwargs):
            return redirect('/users/')
        return render(request, 'users.html')
    

class UserUpdateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'u_create.html')
    
    def post(self, request, *args, **kwargs):
        return render(request, 'users.html')
    

class UserDeleteView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'user_delete.html')
    
    def post(self, request, *args, **kwargs):
        return render(request, 'users.html')


def validate_user(**kwargs):
    return True