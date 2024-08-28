from django.shortcuts import render
from django.views import View
# from django.utils.translation import gettext

USER_DELETED = 'Пользователь успешно удален'

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'index.html')
    

class LogoutView(View):

    def post(self, request, *args, **kwargs):
        return render(request, 'index.html')