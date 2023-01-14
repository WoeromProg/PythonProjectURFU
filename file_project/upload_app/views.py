from django.shortcuts import render
from .models import Book


def index(request):

    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def last_vacancies(request):
    return render(request, 'last_vacancies.html')

def home_page(request):
    # получаем все значения модели
    data = Book.objects.all()
    return render(request, 'home_page.html', {'data': data})