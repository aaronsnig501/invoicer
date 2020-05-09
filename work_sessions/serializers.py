"""
This module is the serializers that will map to any models defined in this
package.
"""
from rest_framework import serializers
from .models import Session


class SessionSerializer(serializers.ModelSerializer):
    """The session serializer

    Serializes all of the fields in the `Session` model
    """

    class Meta:
        model = Session
        fields = '__all__'