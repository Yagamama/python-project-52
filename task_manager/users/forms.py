from django import forms
from .models import User
from django.utils.translation import gettext_lazy
# import django_bootstrap5

class UserForm(forms.ModelForm):

    class Meta:
        
        atr = {'class': 'form-control'}
        FIRST_NAME = gettext_lazy('Имя')
        LAST_NAME = gettext_lazy('Фамилия')
        USERNAME = gettext_lazy('Имя пользователя')
        PASSWORD = gettext_lazy('Пароль')
        PASS_CONFIRM = gettext_lazy('Подтверждение пароля')
        USER_HELP = gettext_lazy('Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.')
        PASS_HELP = gettext_lazy('Ваш пароль должен содержать как минимум 3 символа.')
        PASS_CONFIRM_HELP = gettext_lazy('Для подтверждения введите, пожалуйста, пароль ещё раз.')

        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs=atr|{'placeholder': FIRST_NAME}),
            'last_name': forms.TextInput(attrs=atr|{'placeholder': LAST_NAME}),
            'username': forms.TextInput(attrs=atr|{'placeholder': USERNAME}),
            'password': forms.PasswordInput(attrs=atr|{'placeholder': PASSWORD}),
            'password2': forms.PasswordInput(attrs=atr|{'placeholder': PASS_CONFIRM}),
        }
        labels = {
            'first_name': FIRST_NAME,
            'last_name': LAST_NAME,
            'username': USERNAME,
            'password': PASSWORD,
            'password2': PASS_CONFIRM,
        }
        help_texts = {
            'username': USER_HELP,
            'password': PASS_HELP,
            'password2': PASS_CONFIRM_HELP,
        }
        error_messages = {}
        validators = {}
