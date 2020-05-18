"""generate_invoice.py

This command will be used generate a new invoice in Google Sheets every month.
"""
from datetime import date
import requests
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from invoices.utils.auth import authenticate
from invoices.utils.sheet import SheetFormatMixin
from projects.models import Project


class Command(BaseCommand, SheetFormatMixin):
    """Generate monthly invoices

    This command will generate an invoice every month and create it on Google
    Sheets
    """

    help = "Generate monthly invoices"

    def add_arguments(self, parser):
        """Add arguments to command

        Add additional arguments to the command
        """
        parser.add_argument("project", type=str)
        parser.add_argument("month", type=str)
        parser.add_argument("year", type=str)

    def handle(self, *args, **options):
        """Handle the command
        """
        self.client = authenticate()
        self.worksheet = self.client.open("Invoices").sheet1
        self.project = Project.objects.get(name__icontains=options["project"])
        self.invoicing_date = date.today()
        self.additional_data_url = settings.ADDITIONAL_INVOICE_DATA_URL.format(
            self.project.rate, options["month"], options["year"])

        self.additional_data = requests.get(self.additional_data_url)
        
        self.invoice_data = self.additional_data.json()
        
        self.format_header()
        self.invoicer_name()
        self.add_invoicer_address()
        self.add_submission_date()
        self.add_due_date()
        self.add_additional_titles_to_header()
        self.add_table_headers()
        self.write_formulas_to_invoice()