from django import forms


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
)
class AddBudgetForm(forms.Form):
    budget_name = forms.IntegerField()
    plan = forms.IntegerField()
    id_category = forms.ChoiceField(choices=CATEGORY)