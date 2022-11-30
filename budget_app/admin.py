from django.contrib import admin

from budget_app.models import Contractors, Category, Budget, Invoice

# Register your models here.
admin.site.register(Contractors)
admin.site.register(Category)
admin.site.register(Budget)
admin.site.register(Invoice)