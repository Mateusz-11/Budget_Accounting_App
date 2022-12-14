from django.db import models


class Contractors(models.Model):
    id_contractor = models.BigAutoField(primary_key=True)
    contractor_name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=12)
    street_address = models.CharField(max_length=64)

    def __str__(self):
        return self.contractor_name


class Category(models.Model):
    id_category = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return self.category_name


class Invoice(models.Model):
    id_invoice = models.CharField(max_length=64)
    date_of_issue = models.DateField(null=True)
    sum_amount = models.IntegerField(default=0)
    id_contractor = models.ForeignKey(Contractors, on_delete=models.CASCADE)
    partial_budget = models.ForeignKey("PartialBudget", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.id_invoice


class Service(models.Model):
    id_service = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    amount = models.IntegerField()  # wartosc netto
    id_invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    id_category = models.ManyToManyField(Category)


class PartialBudget(models.Model):
    name = models.CharField(max_length=32)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    id_budget = models.ForeignKey("Budget", on_delete=models.CASCADE)
    plan_amount = models.IntegerField()
    execution_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Budget(models.Model):
    id_budget = models.BigAutoField(primary_key=True)
    name = models.IntegerField(default=2000)
    plan = models.IntegerField(default=0)
    execution = models.IntegerField(default=0)
    id_category = models.ManyToManyField(Category)
    categories_budget = models.ManyToManyField(PartialBudget)

    def __str__(self):
        return str(self.name)
