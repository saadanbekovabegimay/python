from django.shortcuts import render, HttpResponse, redirect
from .models import Vacancy
from company.models import Company
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import VacancyForm





# Create your views here.
def homepage(request):
    if request.method == "POST":
        return HttpResponse("Метод не разрешён, только GET")
    context = {}
    context['vacancies'] = Vacancy.objects.all()[:5]
    context['companies'] = Company.objects.all()[:3]
    return render(request=request, template_name="index.html", context=context)

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


def vacancy_detail(request, id):
    vacancy_object = Vacancy.objects.get(id=id)
    candidates = vacancy_object.candidate.all()
    context = {
        'vacancy': vacancy_object,
        'candidates_list': candidates,
    }
    return render(request, 'vacancy/vacancy_page.html', context)
def search(request):
    word = request.GET["keyword"]
    vacancy_list = Vacancy.objects.filter(title__icontains=word)
    context = {"vacancies": vacancy_list}
    return render(request, 'vacancies.html', context)

def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Неверный логин или пароль")

    return render(request, 'auth/sign_in.html')

def sign_out(request):
    logout(request)
    return redirect(sign_in)
def reg_view(request):
    if request.method == "POST":
        user = User(
            username=request.POST['username']
        )
        user.save()
        user.set_password(request.POST['password'])
        user.save()
        return HttpResponse('Готово')

    return render(
        request,
        'auth/registr.html'
    )

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'index.html', {'vacancies': vacancies})
def add_vacancy(request):
    if request.method == "POST":
        new_vacancy = Vacancy(
            title=request.POST["title"],
            salary=int(request.POST["salary"]),
            description=request.POST["description"],
            email=request.POST["email"],
            contacts=request.POST["contacts"],

        )
        new_vacancy.save()
        return redirect(f'/vacancy/{new_vacancy.id}/')
    return render(request, 'vacancy/vacancy_add.html')

def vacancy_add_via_django_form(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            new_vacancy = form.save()
            return redirect(f'/vacancy/{new_vacancy.id}/')
    vacancy_form = VacancyForm()
    return render(
        request,
        'vacancy/vacancy_django_form.html',
        {"vacancy_form": vacancy_form}
    )
def vacancy_edit(request, id):
    vacancy = Vacancy.objects.get(id=id)
    if request.method == "POST":
        vacancy.title = request.POST["title"]
        vacancy.salary = int(request.POST["salary"])
        vacancy.description = request.POST["description"]
        vacancy.email = request.POST["email"]
        vacancy.contacts = request.POST["contacts"]
        vacancy.save()
        return redirect('resume_info', id=id)
    return render(
        request, 'vacancy/resume_edit_form.html',
        {"vacancy": vacancy}
    )


