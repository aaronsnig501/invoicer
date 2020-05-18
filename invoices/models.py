"""Model module

The models for the invoices app. This model will keep track of all of the
existing invoices, and once the invoice cron task is run, a new record will be
generated here
"""
from django.db import models
from work_sessions.models import Session


class Invoice(models.Model):
    """Invoice model

    This model will keep track of the invoices, their numbers, due dates, etc.

    Each new invoice will be generated with a new unique value, as well as a
    list of the sessions and the total value of all of the work completed. 
    """
    unique_number = models.IntegerField(null=False, blank=False)
    creation_date = models.DateField(auto_now_add=True)
    date_payable = models.DateField(null=True, blank=True)
    sessions = models.ForeignKey(Session, related_name='sessions',
        on_delete=models.CASCADE)
    total_value_earned = models.FloatField(null=False, blank=False)
    location = models.URLField(null=True, blank=True)

    def __str__(self):
        return "{} (created on - {}, due on {})".format(
            unique_number, creation_date, date_payable)
