from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import Book
from .models import DS
from .models import AB
from .models import Skill

def index(request):
    dsdata = DS.objects.all()
    return render(request, 'index.html', {'data': dsdata})

def about(request):
    abdata = AB.objects.all()
    return render(request, 'about.html', {'data': abdata})

def skills(request):
    skilldata = Skill.objects.all()
    return render(request, 'skills.html', {'data': skilldata})

def last_vacancies(request):
    return render(request, 'last_vacancies.html')

def home_page(request):
    # получаем все значения модели
    data = Book.objects.all()
    return render(request, 'home_page.html', {'data': data})