from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    status = serializers.HiddenField(default="New")

    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "message", "status")


class FullContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"
