from django.shortcuts import render
from django.views import View

from budget_app.models import Category


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'budget_app/home_view.html')


class CategoryView(View):
    def get(self, request):
        cat = Category.objects.all()
        ctx = {
            'categories': cat,
        }
        return render(request, 'budget_app/categories_view.html', ctx)