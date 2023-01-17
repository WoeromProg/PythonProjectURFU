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

class SkillsView(TemplateView):

    template_name = 'skills.html'

    def get_context_data(self, **kwargs):
        years = Skill.objects.values('year').distinct().order_by('year')
        ctx = {}

        for y in years:
            ctx[y['year']] = Skill.objects.filter(year=y['year']).order_by('-count')

        return {'data': ctx}
#def skills(request):
    #return render(request, 'skills.html')

def last_vacancies(request):
    return render(request, 'last_vacancies.html')

def home_page(request):
    # получаем все значения модели
    data = Book.objects.all()
    return render(request, 'home_page.html', {'data': data})