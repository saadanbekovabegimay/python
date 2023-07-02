from django.shortcuts import render, HttpResponse
from .models import Vacancy

# Create your views here.
def homepage(request):
    return render(request=request, template_name="index.html")

def about(request):
    return HttpResponse('Найдите работу или работника мечты!')

def contact_view(request):
    return HttpResponse('''
        <div>
            Phone: +3874628734 <br>
            Email: kaium@gmail.com
        </div>
    ''')

def address(request):
    return HttpResponse('''
        <ul>
            <li>г. Бишкек, 7 м-н, 26/1</li>
            <li>г. Ош, Черёмушка, дом 235</li>
        </ul>
    ''')
def company_list(request):
    companies = Company.objects.all()
    context = {"companies": companies}
    return render(request, 'companies.html', context)


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    context = {"vacancies": vacancies}
    context["example"] = "hello"
    return render(request, 'vacancies.html', context)

def vacancy_detail(request, id):
    vacancy_object = Vacancy.objects.get(id=id)
    candidates = vacancy_object.candidate.all()
    context = {
        'vacancy_object': vacancy_object,
        'candidates': candidates,
    }
    return render(request, 'vacancy/vacancy_page.html', context)
