from django.shortcuts import render
import random
from django.utils.translation import gettext

def index(request):
    number = random.randint(12, 100)
    return render(request, 'index.html', context={'number': number})