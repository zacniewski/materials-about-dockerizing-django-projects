from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path, reverse_lazy
from django.views.generic import DeleteView

from .models import Contact
from .views import ContactList, ContactDetail, CreateContact, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    path("contact-list/", staff_member_required(ContactList.as_view()), name="contact_list"),
    path("contact/<int:pk>/update", staff_member_required(ContactDetail.as_view()), name="update_contact"),
    path("contact/<int:pk>/delete", staff_member_required(DeleteView.as_view(
        model=Contact,
        success_url=reverse_lazy("contact_list"),
        template_name="delete_contact.html"
    )),
         name="delete_contact"),
    path("contact/", CreateContact.as_view(), name="create_contact")
]
