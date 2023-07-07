from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm

def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'create_company.html', {'form': form})

def new_company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def company_edit(request, company_id):
    company = Company.objects.get(id=company_id)
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company.name = form.data['name']
            company.date = form.data['date']
            company.workers.set(form.data.getlist('workers'))
            company.save()

            return redirect('new_company_list')
    else:
        form = CompanyForm(
            initial={'name': company.name, 'date': company.date, 'workers': company.workers.all()})
    return render(request, 'edit_company.html', {'form': form, 'company': company})



# Create your views here.
