import pytest

from budget_app.models import Contractors


@pytest.mark.django_db
def test_with_authenticated_client_add_contractor(client, django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)
    # Use this:
    client.force_login(user)
    # Or this:
    # client.login(username=username, password=password)
    data = {
        'contractor_name': "Company X",
        'city': 'City X',
        'zip_code': '00-000',
        'street_address': 'Street X',
    }
    response = client.post('/contractors/', data)
    assert response.status_code == 302
    # assert Contractors.objects.get(contractor_name='Company X') is not None
    # Contractors.refresh_from_db()
    assert Contractors.objects.count() == 1
    # assert len(Contractors.objects.all()) == 1

# @pytest.mark.django_db
# def test_with_authenticated_client_add_contractor(client, django_user_model):
#     username = "user1"
#     password = "bar"
#     user = django_user_model.objects.create_user(username=username, password=password)
#     # Use this:
#     client.force_login(user)
#     # Or this:
#     # client.login(username=username, password=password)
#     response = client.get('/contractors/')
#     assert response.status_code == 200
#
#     response = client.post(reverse("contractors-view"), {
#         'contractor_name': 'Company X',
#         'city': 'City X',
#         'zip_code': '00-000',
#         'street_address': 'Street X',
#     })
#
#     assert response.status_code == 302
#     assert len(Contractors.objects.all()) == 1
#
#     contractor = Contractors.objects.first()
#
#     assert contractor.contractor_name == 'Company X'
#     assert contractor.city == 'City X'
#     assert contractor.zip_code == '00-000'
#     assert contractor.street_address == 'Street X'
