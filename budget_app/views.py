from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from budget_app.forms import AddContractorsForm, AddBudgetForm, AddInvoiceForm, LoginForm
from budget_app.models import Category, Contractors, Budget


# Create your views here.
class HomeView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'budget_app/home_view.html', locals())

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                form.add_error(None, 'Niewłaściwe dane logowania')
        return render(request, 'budget_app/home_view.html', locals())


class LogoutView(View):
    def get(self, request):
        logout(request)
        # return render(request, 'budget_app/home_view.html', locals())
        return redirect('home-view')

class CategoryView(LoginRequiredMixin, View):
    login_url = '/'
    # redirect_field_name = ''
    def get(self, request):
        cat = Category.objects.all()
        ctx = {
            'categories': cat,
        }
        return render(request, 'budget_app/categories_view.html', ctx)


class ContractorsView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = ''
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


class BudgetsView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = ''
    def get(self, request):
        budget = Budget.objects.all()
        ctx = {
            'budget': budget,
        }
        return render(request, 'budget_app/budget_view.html', ctx)


class AddBudgetView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = ''
    def get(self, request):
        form = AddBudgetForm
        ctx = {
            'form': form,
        }
        return render(request, 'budget_app/addbudget_view.html', ctx)

    def post(self, request):
        form = AddBudgetForm(request.POST)
        if form.is_valid():
            pass


class AddInvoiceView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = ''
    def get(self, request):
        form = AddInvoiceForm
        ctx = {
            'form': form,
        }
        return render(request, 'budget_app/addinvoice_view.html', ctx)

    def post(self, request):
        form = AddBudgetForm(request.POST)
        if form.is_valid():
            pass


