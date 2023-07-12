from django.shortcuts import render, redirect, HttpResponse
from .models import Company
from .forms import CompanyForm

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def create_company(request):
    context = {}

    if request.method == "POST":
        company_form = CompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()
            return HttpResponse("Готово!")

    company_form = CompanyForm()
    context["form"] = company_form
    return render(request, 'create_company.html', context)

def company_edit(request, id):
    company_object = Company.objects.get(id=id)

    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company_object)
        if form.is_valid():
            form.save()
            return HttpResponse("Готово!")

    form = CompanyForm(instance=company_object)
    return render(request, "edit_company.html", {"form": form})





