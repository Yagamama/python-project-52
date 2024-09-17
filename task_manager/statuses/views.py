from django.shortcuts import render, redirect
from django.views import View
from .models import Status
from django.utils.translation import gettext_lazy
from django.contrib import messages

BTN_CREATE = gettext_lazy('Создать')
BTN_UPDATE = gettext_lazy('Изменить')
STATUS_UPDATED = gettext_lazy('Статус успешно изменен')
STATUS_CREATED = gettext_lazy('Статус успешно создан')
STATUS_USED = gettext_lazy('Невозможно удалить статус, потому что он используется')
STATUS_DELETED = gettext_lazy('Статус успешно удален')

class StatusesView(View):

    def get(self, request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('/login/')
        st = Status.objects.all().order_by('created_at')
        return render(request, 'statuses/statuses.html', {'statuses': st})


class StatusesCreateView(View):

    def get(self, request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('/login/')
        return render(request, 'statuses/s_create.html', {'btn': BTN_CREATE})

    def post(self, request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('/login/')
        s = Status()
        s.name = request.POST.get('name', 'NoNameStatus')
        s.save()
        messages.success(request, STATUS_CREATED, extra_tags='alert alert-success')
        return redirect('/statuses/')


class StatusesUpdateView(View):

    def get(self, request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('/login/')
        status = Status.objects.get(id=kwargs.get('pk'))
        return render(request, 'statuses/s_create.html', {'status': status, 'btn': BTN_UPDATE})

    def post(self, request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('/login/')
        s = Status.objects.get(id=kwargs.get('pk'))
        s.name = request.POST.get('name', 'NoNameStatus2')
        s.save()
        messages.success(request, STATUS_UPDATED, extra_tags='alert alert-success')
        return redirect('/statuses/')


class StatusesDeleteView(View):

    def get(self, request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('/login/')
        status = Status.objects.get(id=kwargs.get('pk'))
        return render(request, 'statuses/s_delete.html', {'status': status})

    def post(self, request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('/login/')
        s = Status.objects.get(id=kwargs.get('pk'))
        s.delete()
        messages.success(request, STATUS_DELETED, extra_tags='alert alert-success')
        return redirect('/statuses/')
