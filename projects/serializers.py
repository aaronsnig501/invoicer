"""
This module is the serializers that will map to any models defined in this
package.
"""
from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """The project serializer

    Serializes all of the fields in the `Project` model
    """

    class Meta:
        model = Project
        fields = '__all__'