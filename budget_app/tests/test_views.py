import pytest
from django.urls import reverse


def test_home_view(client):
    response = client.get('')
    assert response.status_code == 200


def test_categories_view(client):
    response = client.get('/categories/')
    assert response.status_code == 302


def test_budgets_view(client):
    response = client.get('/budgets/')
    assert response.status_code == 302


def test_partialbudget_view(client):
    response = client.get('/partialbudget/')
    assert response.status_code == 302


def test_logout_view(client):
    response = client.get('/logout/')
    assert response.status_code == 302  # redirect


def test_with_authenticated_client_categories_view(client, django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)
    # Use this:
    client.force_login(user)
    # Or this:
    # client.login(username=username, password=password)
    response = client.get('/categories/')
    assert response.status_code == 200


def test_with_authenticated_client_budgets_view(client, django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)
    # Use this:
    client.force_login(user)
    # Or this:
    # client.login(username=username, password=password)
    response = client.get('/budgets/')
    assert response.status_code == 200


def test_with_authenticated_client_partialbudget_view(client, django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)
    # Use this:
    client.force_login(user)
    # Or this:
    # client.login(username=username, password=password)
    response = client.get('/partialbudget/')
    assert response.status_code == 200
