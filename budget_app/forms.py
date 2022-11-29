from django import forms


class AddContractorsForm(forms.Form):
    contractor_name = forms.CharField(max_length=255)
    city = forms.CharField(max_length=64)
    zip_code = forms.CharField(max_length=12)
    street_address = forms.CharField(max_length=64)