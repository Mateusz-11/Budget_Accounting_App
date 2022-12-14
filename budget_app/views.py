from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView

from budget_app.forms import AddContractorsForm, AddBudgetForm, AddInvoiceForm, LoginForm, ChooseInvoicesForm, \
    ChoosePartialBudgetForm, AddPartialBudgetForm, AddServiceForm
from budget_app.models import Category, Contractors, Budget, Invoice, PartialBudget, Service


class HomeView(View):
    """
    It's main view of application. On it, User can log in to app.
    """
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
    """
    It's view used to logout Users.
    """
    def get(self, request):
        logout(request)
        # return render(request, 'budget_app/home_view.html', locals())
        return redirect('home-view')


class CategoryView(LoginRequiredMixin, View):
    """
    It's view with table of all Categoris.
    """
    def get(self, request):
        cat = Category.objects.all()
        ctx = {
            'categories': cat,
        }
        return render(request, 'budget_app/categories_view.html', ctx)


class ContractorsView(LoginRequiredMixin, View):
    """
    It's view with form to add Contractors and table with all Contractors.
    """
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
    """
    It's view with all created Budgets.
    """
    # login_url = '/'
    # redirect_field_name = ''
    def get(self, request):
        budget = Budget.objects.all()
        ctx = {
            'budget': budget,
        }
        return render(request, 'budget_app/budget_view.html', ctx)


class AddBudgetView(LoginRequiredMixin, View):
    """
    It's view with form to add budget.
    """
    def get(self, request):
        form = AddBudgetForm
        ctx = {
            'form': form,
        }
        return render(request, 'budget_app/addbudget_view.html', ctx)

    def post(self, request):
        form = AddBudgetForm(request.POST)
        if form.is_valid():
            b = Budget()
            name = form.cleaned_data.get('budget_name')
            b.name = name
            b.save()
            return redirect('budgets-view')
        return render(request, 'budget_app/addbudget_view.html', locals())


class AddInvoiceView(LoginRequiredMixin, View):
    """
    It's view with form to add invoice.
    """
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
            contractor = form.cleaned_data.get('contractor')
            date_of_issue = form.cleaned_data.get('date_of_issue')
            partial_budget = form.cleaned_data.get('partial_budget')
            i.id_invoice = id_invoice
            i.id_contractor = contractor
            i.date_of_issue = date_of_issue
            i.partial_budget = partial_budget
            i.save()
            return redirect('invoices-view')
        return render(request, 'budget_app/addinvoice_view.html', locals())


class InvoicesView(LoginRequiredMixin, View):
    """
    It's view with all invoices.
    """
    def get(self, request):
        form = ChooseInvoicesForm
        invoices1 = Invoice.objects.all()
        paginator = Paginator(invoices1, 3)  # Show 3 contacts per page.

        page_number = request.GET.get('page')
        invoices = paginator.get_page(page_number)
        ctx = {
            'form': form,
            'invoices': invoices,
            'suma': invoices[0].service_set.all().aggregate(Sum("amount")),
        }
        return render(request, 'budget_app/invoices_view.html', ctx)

    def post(self, request):
        form = ChooseInvoicesForm(request.POST)
        if form.is_valid():
            pb = form.cleaned_data.get('partial_budget')
            invoices = Invoice.objects.filter(partial_budget=pb)
            ctx = {
                'invoices': invoices,
            }
            return render(request, 'budget_app/invoices_view.html', locals())
        return render(request, 'budget_app/invoices_view.html', locals())


class PartialBudgetView(LoginRequiredMixin, View):
    """
    It's view with all Partial Budget.
    """
    def get(self, request):
        form = ChoosePartialBudgetForm
        partialbudget = PartialBudget.objects.all()
        pb_sums = [p.invoice_set.aggregate(Sum("sum_amount")) for p in partialbudget]
        ctx = {
            'form': form,
            'partialbudget': partialbudget,
            'pb_sums': pb_sums,
        }
        return render(request, 'budget_app/partialbudget_view.html', ctx)

    def post(self, request):
        form = ChoosePartialBudgetForm(request.POST)
        if form.is_valid():
            budget = form.cleaned_data.get('id_budget')
            partialbudget = PartialBudget.objects.filter(id_budget=budget)
            ctx = {
                'partialbudget': partialbudget,
            }
            return render(request, 'budget_app/partialbudget_view.html', locals())
        return render(request, 'budget_app/partialbudget_view.html', locals())


class AddPartialBudgetView(LoginRequiredMixin, View):
    """
    It's view with form to add a Partial Budgets.
    """
    def get(self, request):
        form = AddPartialBudgetForm
        ctx = {
            'form': form,
        }
        return render(request, 'budget_app/addpartialbudget_view.html', ctx)

    def post(self, request):
        form = AddPartialBudgetForm(request.POST)
        if form.is_valid():
            p = PartialBudget()
            name = form.cleaned_data.get('name')
            plan_amount = form.cleaned_data.get('plan_amount')
            id_budget = form.cleaned_data.get('id_budget')
            cat = form.cleaned_data.get('id_category')
            # category = Category.objects.get(id_category=cat)
            p.name = name
            p.plan_amount = plan_amount
            p.id_budget = id_budget
            p.id_category = cat
            p.save()
            return redirect('partialbudget-view')
        return render(request, 'budget_app/addpartialbudget_view.html', locals())


class CreateServiceView(CreateView):
    model = Service
    fields = ["name", "amount", "id_invoice", "id_category"]

    def get_success_url(self):
        return reverse('createservice-view')

#
# class CreateServiceView(CreateView):
#     """
#     It's view with form to create service.
#     """
#     def get(self, request):
#         form = AddServiceForm
#         ctx = {
#             'form': form,
#         }
#         return render(request, 'budget_app/service_form.html', ctx)
#
#     def post(self, request):
#         form = AddServiceForm(request.POST)
#         if form.is_valid():
#             p = Service()
#             name = form.cleaned_data.get('name')
#             amount = form.cleaned_data.get('amount')
#             id_invoice = form.cleaned_data.get('id_invoice')
#             id_category = form.cleaned_data.get('id_category')
#             p.name = name
#             p.amount = amount
#             p.id_invoice = id_invoice
#             p.id_category = id_category
#             p.save()
#
#
#             return redirect('createservice-view')
#         return render(request, 'budget_app/service_form.html', locals())
