"""
This model will store the information relating to sessions and the total
billable per each session.

A session is considered to be the amount of work that was done in a time. An
example of this could be a meeting, a planning session, working a piece of
functionality, or writing tests/documentation, etc.

All sessions of work most be carried out as a part of a project. The project
determines the rate of pay and any other additional information related to the
project.
"""
from django.db import models
from projects.models import Project


class Session(models.Model):
    """The session model

    Stores information about the length of the individual sessions, and the
    total billable for each session.

    Args:
        date (date): The date the session occured on
        duration (timedelate): The length of time that this work was carried
        out for
        total_billable (float): The total amount of money that was earned for
        this work session
        project (Project): The project that this work was carried out for
    """

    date = models.DateField(null=False, blank=False)
    duration = models.DurationField(null=False, blank=False)
    total_billable = models.DecimalField(
        max_digits=5, decimal_places=2, null=False, blank=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} - {}".format(self.date, self.total_billable)