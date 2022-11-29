from django.shortcuts import render, redirect
from django.views import View

from budget_app.forms import AddContractorsForm
from budget_app.models import Category, Contractors, Budget


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'budget_app/home_view.html')


class CategoryView(View):
    def get(self, request):
        cat = Category.objects.all()
        ctx = {
            'categories': cat,
        }
        return render(request, 'budget_app/categories_view.html', ctx)

class ContractorsView(View):
    def get(self, request):
        form = AddContractorsForm
        contractors = Contractors.objects.all()
        ctx = {
            'form': form,
            'contractors': contractors,
        }
        return render(request, 'budget_app/contractors_view.html', ctx)

    def post(self, request):
        form = AddContractorsForm(request.POST)
        if form.is_valid():
            c = Contractors()
            contractor_name = form.cleaned_data.get('contractor_name')
            city = form.cleaned_data.get('city')
            zip_code = form.cleaned_data.get('zip_code')
            street_address = form.cleaned_data.get('street_address')
            c.contractor_name = contractor_name
            c.city = city
            c.zip_code = zip_code
            c.street_address = street_address
            c.save()
            return redirect('contractors-view')
        return render(request, 'budget_app/contractors_view.html', locals())


class BudgetsView(View):
    def get(self, request):
        budget = Budget.objects.all()
        ctx = {
            'budget': budget,
        }
        return render(request, 'budget_app/budget_view.html', ctx)


class AddBudgetsView(View):
    def get(self, request):
        form = AddBudgetForm
        ctx = {
            'form': form,
        }
        return render(request, 'budget_app/addbudget_view.html', ctx)