from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView

from budget_app.forms import AddContractorsForm, AddBudgetForm, AddInvoiceForm, LoginForm, ChooseInvoicesForm, \
    ChoosePartialBudgetForm
from budget_app.models import Category, Contractors, Budget, Invoice, PartialBudget, Service


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
    def get(self, request):
        cat = Category.objects.all()
        ctx = {
            'categories': cat,
        }
        return render(request, 'budget_app/categories_view.html', ctx)


class ContractorsView(LoginRequiredMixin, View):
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
    # login_url = '/'
    # redirect_field_name = ''
    def get(self, request):
        budget = Budget.objects.all()
        ctx = {
            'budget': budget,
        }
        return render(request, 'budget_app/budget_view.html', ctx)


class AddBudgetView(LoginRequiredMixin, View):
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
    def get(self, request):
        form = AddInvoiceForm
        ctx = {
            'form': form,
        }
        return render(request, 'budget_app/addinvoice_view.html', ctx)

    def post(self, request):
        form = AddInvoiceForm(request.POST)
        if form.is_valid():
            i = Invoice()
            id_invoice = form.cleaned_data.get('id_invoice')
            id_contractor = form.cleaned_data.get('contractor')
            category_name = form.cleaned_data.get('category')
            date_of_issue = form.cleaned_data.get('date_of_issue')
            i.id_invoice = id_invoice
            i.id_contractor = id_contractor
            i.category_name = category_name
            i.date_of_issue = date_of_issue
            i.save()
            return redirect('invoices-view')
        return render(request, 'budget_app/addinvoice_view.html', locals())


class InvoicesView(LoginRequiredMixin, View):
    def get(self, request):
        form = ChooseInvoicesForm
        invoices = Invoice.objects.all()
        ctx = {
            'form': form,
            'invoices': invoices,
            'suma' : invoices[0].service_set.all().aggregate(Sum("amount")),
        }
        return render(request, 'budget_app/invoices_view.html', ctx)

    def post(self, request):
        form = ChooseInvoicesForm(request.POST)
        if form.is_valid():
            cat = form.cleaned_data.get('id_category')
            invoices = Invoice.objects.filter(category_name=cat)
            ctx = {
                'invoices': invoices,
            }
            return render(request, 'budget_app/invoices_view.html', locals())
        return render(request, 'budget_app/invoices_view.html', locals())

class PartialBudgetView(LoginRequiredMixin, View):
    def get(self, request):
        form = ChoosePartialBudgetForm
        partialbudget = PartialBudget.objects.all()
        ctx = {
            'form': form,
            'partialbudget': partialbudget,
        }
        return render(request, 'budget_app/partialbudget_view.html', ctx)

    def post(self, request):
        form = ChoosePartialBudgetForm(request.POST)
        if form.is_valid():
            cat = form.cleaned_data.get('id_category')
            partialbudget = PartialBudget.objects.filter(id_category=cat)
            ctx = {
                'partialbudget': partialbudget,
            }
            return render(request, 'budget_app/partialbudget_view.html', locals())
        return render(request, 'budget_app/partialbudget_view.html', locals())


class CreateServiceView(CreateView):
    model = Service
    fields = ["name", "amount", "id_invoice", "id_category"]
    def get_success_url(self):
        return reverse('createservice-view')