
"""
The projects views module.

All of the interactions with the projects models will happen through the views
defined here. In general, these views will require authentication as this is
sensitive information that likely shouldn't be shared with anyone.
"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewset(viewsets.ReadOnlyModelViewSet):
    """The projects viewset

    The view that will handle the interactions with the `Projects` model. This
    viewset is ReadOnly as records will generally be automated and can also be
    created in the admin panel. As of yet there is no requirement to create
    projects from this view.

    Returns:
        JSON Array: Returns an array of JSON objects containing the fields
        specified in the `serializer_class`
    """

    permission_classes = (IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer