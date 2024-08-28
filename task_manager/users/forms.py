from django import forms
from .models import Users
from django.utils.translation import gettext
# import django_bootstrap5

class UserForm(forms.ModelForm):

    class Meta:
        
        atr = {'class': 'form-control'}

        model = Users
        fields = ['first_name', 'last_name', 'username', 'password', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs=atr),
            'last_name': forms.TextInput(attrs=atr),
            'username': forms.TextInput(attrs=atr),
            'password': forms.PasswordInput(attrs=atr),
            'password2': forms.PasswordInput(attrs=atr),
        }
        labels = {
            'first_name': gettext('Имя'),
            'last_name': gettext('Фамилия'),
            'username': gettext('Имя пользователя'),
            'password': gettext('Пароль'),
            'password2': gettext('Подтверждение пароля'),
        }
        help_text = {
            'username': gettext('Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.'),
            'password': gettext('Ваш пароль должен содержать как минимум 3 символа.'),
            'password2': gettext('Для подтверждения введите, пожалуйста, пароль ещё раз.'),
        }
