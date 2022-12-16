from django import forms

from budget_app.models import Category, Budget, Contractors, PartialBudget, Invoice


class AddContractorsForm(forms.Form):
    contractor_name = forms.CharField(max_length=255)
    city = forms.CharField(max_length=64)
    zip_code = forms.CharField(max_length=12)
    street_address = forms.CharField(max_length=64)


class AddBudgetForm(forms.Form):
    budget_name = forms.IntegerField()


class AddPartialBudgetForm(forms.Form):
    name = forms.CharField(max_length=32)
    id_category = forms.ModelChoiceField(queryset=Category.objects.all())
    id_budget = forms.ModelChoiceField(queryset=Budget.objects.all())
    plan_amount = forms.IntegerField()


class AddInvoiceForm(forms.Form):
    id_invoice = forms.CharField(max_length=64)
    contractor = forms.ModelChoiceField(queryset=Contractors.objects.all())
    # category = forms.ModelChoiceField(queryset=Category.objects.all())
    date_of_issue = forms.DateField(widget=forms.SelectDateWidget)
    # date_of_issue = forms.DateField()
    partial_budget = forms.ModelChoiceField(queryset=PartialBudget.objects.all())


class AddServiceForm(forms.Form):
    name = forms.CharField(max_length=64)
    amount = forms.IntegerField()
    id_invoice = forms.ModelChoiceField(queryset=Invoice.objects.all())
    id_category = forms.ModelChoiceField(queryset=Category.objects.all())


class LoginForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)


class ChooseInvoicesForm(forms.Form):
    partial_budget = forms.ModelChoiceField(queryset=PartialBudget.objects.all())


class ChoosePartialBudgetForm(forms.Form):
    id_budget = forms.ModelChoiceField(queryset=Budget.objects.all())
