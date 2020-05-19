"""generate_invoice.py

This command will be used generate a new invoice in Google Sheets every month.
"""
from datetime import timedelta
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

        This command will retrieve the data from the API, add all of the data
        to the Google Sheet and generate a matching record in Invoice model
        """
        # Authenticate with Google and get the worksheet
        self.client = authenticate()
        self.worksheet = self.client.open("Invoices").sheet1

        # Get the project details
        self.project = Project.objects.get(name__icontains=options["project"])

        # Set the date information for this invoice
        self.invoicing_date = date.today().strftime("%d/%m/%Y")
        self.due_date = date.today() + timedelta(days=30)

        # Get the additional data from the API
        self.additional_data_url = settings.ADDITIONAL_INVOICE_DATA_URL.format(
            self.project.rate, options["month"], options["year"])
        self.additional_data = requests.get(self.additional_data_url)
        self.invoice_data = self.additional_data.json()
        self.total_billable = sum(entry["total_billable"] for entry in self.invoice_data)
        
        # Update the Invoice in Sheets
        self.format_header()
        self.invoicer_name()
        self.add_invoicer_address()
        self.add_submission_date()
        self.add_due_date()
        self.add_additional_titles_to_header()
        self.add_table_headers()
        self.write_formulas_to_invoice()
        self.write_the_total_billable()