from django import forms

from budget_app.models import Category, Budget, Contractors


class AddContractorsForm(forms.Form):
    contractor_name = forms.CharField(max_length=255)
    city = forms.CharField(max_length=64)
    zip_code = forms.CharField(max_length=12)
    street_address = forms.CharField(max_length=64)

CATEGORY = (
    (1, "Paid advertising"),
    (3, "Search Engine Optimization"),
    (4, "Photography Services"),
    (5, "Content Marketing"),
    (6, "Graphic Services"),
    (7, "Movie Services"),
)

class AddBudgetForm(forms.Form):
    budget_name = forms.IntegerField()
    plan = forms.IntegerField()
    id_category = forms.ModelChoiceField(queryset=Category.objects.all())
    # id_category = forms.ChoiceField(choices=CATEGORY)  # old version


class AddInvoiceForm(forms.Form):
    budget = forms.ModelChoiceField(queryset=Budget.objects.all())
    service_name = forms.CharField(max_length=64)
    contractor_name = forms.ModelChoiceField(queryset=Contractors.objects.all())
    id_category = forms.ModelChoiceField(queryset=Category.objects.all())
    amount = forms.IntegerField()
    date_of_issue = forms.DateField()


class LoginForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)
