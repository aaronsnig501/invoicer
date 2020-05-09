"""
The session views module.

All of the interactions with the sessions models will happen through the views
defined here. In general, these views will require authentication as this is
sensitive information that likely shouldn't be shared with anyone.
"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Session
from .serializers import SessionSerializer


class SessionViewset(viewsets.ReadOnlyModelViewSet):
    """The session viewset

    The view that will handle the interactions with the `Session` model. This
    viewset is ReadOnly as records will generally be automated and can also be
    created in the admin panel. As of yet there is no requirement to create
    sessions from this view.

    Returns:
        JSON Array: Returns an array of JSON objects containing the fields
        specified in the `serializer_class`
    """

    permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
