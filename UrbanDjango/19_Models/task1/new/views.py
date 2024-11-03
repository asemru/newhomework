from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News
# Create your views here.

def index(reqwest):
    post = News.objects.all().order_by('-data')
    paginator = Paginator(post, 3)
    page_number = reqwest.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(reqwest, 'code.html', {'page_obj': page_obj})

