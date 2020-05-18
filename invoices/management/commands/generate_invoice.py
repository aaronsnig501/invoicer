"""generate_invoice.py

This command will be used generate a new invoice in Google Sheets every month.
"""
from datetime import date
from django.core.management.base import BaseCommand, CommandError
from invoices.utils.auth import authenticate
from invoices.utils.sheet import SheetFormatMixin


class Command(BaseCommand, SheetFormatMixin):
    """Generate monthly invoices

    This command will generate an invoice every month and create it on Google
    Sheets
    """

    help = "Generate monthly invoices"

    def handle(self, *args, **kwargs):
        """Handle the command
        """
        self.client = authenticate()
        self.worksheet = self.client.open("Invoices").sheet1
        self.format_header()