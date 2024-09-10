from django.shortcuts import render, redirect
from django.views import View
from .models import Status
from django.utils.translation import gettext_lazy

BTN_CREATE = gettext_lazy('Создать')
BTN_UPDATE = gettext_lazy('Изменить')


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
        return redirect('/statuses/')
