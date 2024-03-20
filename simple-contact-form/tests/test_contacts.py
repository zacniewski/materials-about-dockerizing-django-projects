import pytest
from model_bakery import baker

from django.urls import reverse
from pytest_drf import APIViewTest, UsesGetMethod, Returns200
from pytest_lambda import lambda_fixture
from rest_framework.test import APITestCase

from contacts.models import Contact
from contacts.serializers import FullContactSerializer

contact_data = {
    "name": "John",
    "email": "johny@media.com",
    "subject": "Other",
    "message": "Testing contact",
    "status": "New"
}


# testing 'home_page' view
def test_with_no_authenticated_client(client, django_user_model):
    response = client.get('/')
    assert response.status_code == 200


# testing 'contact_list' view
def test_with_authenticated_client(admin_client, django_user_model):
    response = admin_client.get('/contact-list')
    assert response.status_code == 301


# testing 'contact_list' view
@pytest.mark.django_db
def test_list_of_contacts(admin_client):
    url = reverse('contact_list')
    response = admin_client.get(url)

    assert response.status_code == 200
    assert response.data["contacts"] is not None


# testing 'Contact' model
@pytest.mark.django_db
def test_create_contact_1():
    category = Contact.objects.create(
        name="John",
        email="john@media.com",
        subject="App support",
        message="Testing John",
        status="New"
    )
    assert category.status == "New"


# testing 'create_contact' view
@pytest.mark.django_db
def test_create_contact_2(admin_client):
    url = "/contact/"
    payload = {
        "name": "Terry Johns",
        "email": "terry@media.com",
        "subject": "Other",
        "message": "Testing Terry",
        "status": "Resolved",
        "id": 100
    }
    response = admin_client.post(url, payload)
    assert response.status_code == 200


# testing 'contact_list' view
@pytest.mark.django_db
def test_get_contacts(admin_client, create_contact):
    response = admin_client.get(reverse('contact_list'))
    assert response.status_code == 200


# testing 'home_page' view with pytest-drf
class TestHelloWorld(
    APIViewTest,
    UsesGetMethod,
    Returns200,
):
    url = lambda_fixture(lambda: reverse("home_page"))


# testing 'home_page' view with APITestCase
@pytest.mark.django_db
class TestSecond(APITestCase):
    def test_home_page(self):
        get_data = self.client.get('/')
        self.assertEqual(200, get_data.status_code)


# testing 'create_contact' view
@pytest.mark.django_db
def test_post_contact(admin_client):
    # send a POST request to the CreateAPIView with the data for a new contact
    response = admin_client.post('/contact', data=contact_data)
    # assert that the response status code is correct
    assert response.status_code == 301


# testing 'contact_detail' view
@pytest.mark.django_db
def test_retrieve_contact(admin_client):
    # send a request to the RetrieveUpdateDestroyAPIView for an individual contact
    contact1 = baker.make(Contact)
    serializer = FullContactSerializer(contact1)
    response = admin_client.get(f'/contact/{contact1.id}/update')

    # assert that the response status code is correct
    assert response.status_code == 200
    # assert that the returned data is correct
    assert response.data["contact"].name == serializer.data["name"]


# testing 'contact_detail' view
@pytest.mark.django_db
def test_destroy_contact(admin_client):
    # send a DELETE request to the RetrieveUpdateDestroyAPIView for an individual person
    contact2 = baker.make(Contact)
    response = admin_client.delete(f'/contact/{contact2.id}/delete')
    # assert that the response status code is correct
    assert response.status_code == 302
    # assert that the contact is not in the list of contacts
    response2 = admin_client.get(reverse('contact_list'))
    assert response2.status_code == 200
    assert Contact.objects.filter(id=contact2.id).first() is None
