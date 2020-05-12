"""
The models for the `Projects` app.

These models will house any and all information relating to a project

A project is considered to be a specific project that you are working on. For example,
you may be working on one, or many projects for a company, and each project may have a
specific hourly rate.
"""
from django.db import models


class Project(models.Model):
    """
    Projects will have a name and and an hourly rate

    Args:
        name (str): The name of the project being worked on
        rate (int): The hourly rate being earned
    """

    name = models.CharField(max_length=50)
    rate = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.name, self.rate)