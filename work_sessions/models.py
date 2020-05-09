"""
This model will store the information relating to sessions and the total
billable per each session.

A session is considered to be the amount of work that was done in a time. An
example of this could be a meeting, a planning session, working a piece of
functionality, or writing tests/documentation, etc.
"""
from django.db import models


class Session(models.Model):
    """The session model

    Stores information about the length of the individual sessions, and the
    total billable for each session
    """

    date = models.DateField(null=False, blank=False)
    duration = models.DurationField(null=False, blank=False)
    total_billable = models.DecimalField(
        max_digits=5, decimal_places=2, null=False, blank=False)
    
    def __str__(self):
        return "{} - {}".format(self.date, self.total_billable)