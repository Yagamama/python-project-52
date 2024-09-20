from typing import Any
from django import forms
from .models import Task
from django.utils.translation import gettext_lazy
# import django_bootstrap5

class TaskForm(forms.ModelForm):

    class Meta:
        
        atr = {'class': 'form-control'}
        NAME = gettext_lazy('Имя')
        AUTHOR = gettext_lazy('Автор')
        DESCRIPTION = gettext_lazy('Описание')
        STATUS = gettext_lazy('Статус')
        EXECUTOR = gettext_lazy('Исполнитель')
        TAG = gettext_lazy('Метки')

        model = Task
        fields = ['name', 'description', 'status', 'executor', 'author']  #, 'tag']
        widgets = {
            'name': forms.TextInput(attrs=atr|{'placeholder': NAME}),
            'description': forms.Textarea(attrs=atr|{'placeholder': DESCRIPTION}),
            'status': forms.Select(attrs=atr|{'placeholder': STATUS}),
            'executor': forms.Select(attrs=atr|{'placeholder': EXECUTOR}),
            'author': forms.Select(attrs={'display': None}),
            # 'tag': forms.Select(attrs=atr|{'placeholder': TAG}),
        }
        labels = {
            'name': NAME,
            'description': DESCRIPTION,
            'status': STATUS,
            'executor': EXECUTOR,
            # 'tag': TAG,
        }
