from django.db import models


class Contractors(models.Model):
    id_contractor = models.BigAutoField(primary_key=True)
    contractor_name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=12)
    street_address = models.CharField(max_length=64)


class Invoice(models.Model):
    nr_invoice = models.CharField(primary_key=True, max_length=64)
    date_of_issue = models.DateField()
    id_contractor = models.ForeignKey(Contractors, on_delete=models.CASCADE)


class Category(models.Model):
    id_category = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=32)


class Service(models.Model):
    id_service = models.BigAutoField(primary_key=True)
    service_name = models.CharField(max_length=64)
    amount = models.IntegerField()  # wartosc netto
    nr_invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    id_category = models.ManyToManyField(Category)


class Budget(models.Model):
    id_budget = models.BigAutoField(primary_key=True)
    budget_name = models.IntegerField
    plan = models.IntegerField(default=0)
    execution = models.IntegerField(default=0)
    id_category = models.ManyToManyField(Category)
