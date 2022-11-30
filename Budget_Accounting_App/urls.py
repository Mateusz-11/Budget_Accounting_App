"""Budget_Accounting_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from budget_app.views import HomeView, LogoutView, CategoryView, ContractorsView, BudgetsView, AddBudgetView, AddInvoiceView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home-view"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('categories/', CategoryView.as_view(), name="categories-view"),
    path('contractors/', ContractorsView.as_view(), name="contractors-view"),
    path('budgets/', BudgetsView.as_view(), name="budgets-view"),
    path('add-budget/', AddBudgetView.as_view(), name="addbudget-view"),
    path('add-invoice/', AddInvoiceView.as_view(), name="addinvoice-view"),

]
