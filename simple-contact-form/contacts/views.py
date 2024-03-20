from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from rest_framework import generics, permissions
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response

from .models import Contact
from .serializers import ContactSerializer, FullContactSerializer


class HomePageView(TemplateView):
    template_name = "home_page.html"
    success_url = reverse_lazy("create_contact")


class ContactList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "contact_list.html"

    def get(self, request):
        queryset = Contact.objects.all()
        paginate_queryset = self.paginator.paginate_queryset(queryset, request)
        serialize_pagination = FullContactSerializer(paginate_queryset, many=True).data
        data = self.paginator.get_paginated_response(serialize_pagination).data
        return Response({'contacts': data})

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "update_contact.html"

    def get(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        serializer = FullContactSerializer(contact)
        return Response({'serializer': serializer, 'contact': contact})

    def post(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        serializer = FullContactSerializer(contact, data=request.data)
        if not serializer.is_valid():
            messages.error(request, "Something went wrong, check all the fields!")
            return Response({'serializer': serializer, 'contact': contact})
        serializer.save()
        messages.success(request, "The contact has been updated!")
        return redirect("contact_list")

    def delete(self, request, pk, format=None):
        contact = self.get_object(pk)
        contact.delete()
        messages.info(request, "The contact has been deleted!")
        return redirect("contact_list")


class CreateContact(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (permissions.IsAuthenticated,)
    template_name = "create_contact.html"
    success_url = "create_contact"

    def get(self, request):
        serializer = ContactSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "The contact has been created!")
            return redirect("create_contact")
        else:
            messages.error(request, "Something went wrong, check all the fields below!")
            return Response({"serializer": serializer, "data": serializer.data})
