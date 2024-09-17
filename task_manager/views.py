from django.shortcuts import render, redirect
from django.views import View
from .users.models import User
from django.utils.translation import gettext_lazy
from django.contrib import messages

USER_LOGINED = gettext_lazy('Вы залогинены')
USER_LOGOUT = gettext_lazy('Вы разлогинены')
USER_WRONG_DATA = gettext_lazy('Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть чувствительны к регистру.')

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        name = request.POST['username']
        password = request.POST['password']
        filt = User.objects.filter(username=name).all()
        if len(filt) > 0:
            if filt[0].password == password:
                request.session['username'] = name
                request.session['user_id'] = filt[0].id
                messages.success(request, USER_LOGINED, extra_tags='alert alert-success')
                return redirect('/')
        return render(request, 'login.html', {'name': name, 'errors': [USER_WRONG_DATA]})
    

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        request.session.clear()
        messages.success(request, USER_LOGOUT, extra_tags='alert alert-info')
        return render(request, 'index.html')