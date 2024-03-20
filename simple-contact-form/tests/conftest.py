import pytest

from contacts.models import Contact


@pytest.fixture
def create_contact():
    payload = {
        "name": "Terry Johns",
        "email": "terry@media.com",
        "subject": "Other",
        "message": "Testing Terry",
        "status": "Resolved"
    }
    record = Contact.objects.create(**payload)
    return record
