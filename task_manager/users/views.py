from django.shortcuts import render
from django.views import View

# def index(request):
#     return render(request, 'users.html')

class UsersView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users.html')
    

class UserCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'u_create.html')
    
    def post(self, request, *args, **kwargs):
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