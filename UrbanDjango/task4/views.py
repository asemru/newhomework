from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def index(request):
    text = 'hellow'
    text2 = ['PayDay2', 'Cyberpunk2077', 'Atomic Heart']
    context = {
        'text': text,
        'text2': text2,
    }
    return render(request, 'videogames.html', context)



