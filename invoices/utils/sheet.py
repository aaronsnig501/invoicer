"""sheet.py

Handle the formatting of the Google Sheet
"""

from datetime import date
from gspread_formatting  import (
    cellFormat, color, textFormat, format_cell_ranges)
from django.conf import settings


class SheetFormatMixin:
    """SheetFormatMixin

    A mixin class that will provide the mapping and formatting for the Google
    Sheet. This is the class that will define where each piece of information
    belongs on the invoice
    """
    SHEET_START_POINT = "A1"
    LAST_COLUMN = "H"

    FULL_NAME_CELL = "B3"
    ADDRESS_LINE_ONE = "B4"
    ADDRESS_LINE_TWO = "B5"
    ADDRESS_LINE_THREE = "B6"
    PHONE = "B7"

    TITLE = "B9"
    SUBMISSION_DATE = "B10"

    INVOICE_FOR = "B12"
    INVOICE_FOR_FULL_NAME_CELL = "B13"
    INVOICE_FOR_ADDRESS_LINE_ONE = "B14"
    INVOICE_FOR_ADDRESS_LINE_TWO = "B15"
    INVOICE_FOR_ADDRESS_LINE_THREE = "B16"

    PAYABLE_TO_TITLE = "D12"
    PAYABLE_TO = "D13"
    INVOICE_NUMBER_TITLE = "F12"
    INVOICE_NUMBER = "F13"
    PROJECT_TITLE = "D15"
    PROJECT = "D16"
    DUE_DATE_TITLE = "F15"
    DUE_DATE = "F16"

    TABLE_HEADER_ROW = "19"
    DESCRIPTION_HEADER = "B" + TABLE_HEADER_ROW
    RATE_HEADER = "E" + TABLE_HEADER_ROW
    HOURS_HEADER = "F" + TABLE_HEADER_ROW
    TOTAL_HEADER = "G" + TABLE_HEADER_ROW
    TABLE_FIRST_ROW = "20"
    TABLE_START_COLUMN = "B"

    def format_header(self):
        """Format the header of the invoice.

        Turns the first row of the invoice blue
        """
        header_format = cellFormat(
            backgroundColor=color(0, 0, 0.625)
        )

        format_cell_ranges(self.worksheet, [(
            self.SHEET_START_POINT + ":" + self.LAST_COLUMN + "1", header_format
        )])
    
    def invoicer_name(self):
        """Add the main title

        Add the name of the invoicer has a heading
        """
        self.worksheet.update(self.FULL_NAME_CELL, settings.FULL_NAME)
        self.worksheet.format(self.FULL_NAME_CELL, {
            "textFormat": {
                "foregroundColor": {
                    "red": 0,
                    "green": 0,
                    "blue": 0.95
                },
                "fontFamily": "Roboto",
                "fontSize": 20
            }
        })
    
    def add_invoicer_address(self):
        """Add invoicer address

        The address appears in multiple locations on the sheet, so we'll add
        both here
        """
        self.worksheet.update(
            self.ADDRESS_LINE_ONE, settings.ADDRESS_LINE_ONE)
        self.worksheet.update(
            self.ADDRESS_LINE_TWO, settings.ADDRESS_LINE_TWO)
        self.worksheet.update(
            self.ADDRESS_LINE_THREE, settings.ADDRESS_LINE_THREE)
        self.worksheet.update(
            self.PHONE, settings.PHONE)

        self.worksheet.update(
            self.INVOICE_FOR_FULL_NAME_CELL, settings.FULL_NAME)        
        self.worksheet.update(
            self.INVOICE_FOR_ADDRESS_LINE_ONE, settings.ADDRESS_LINE_ONE)
        self.worksheet.update(
            self.INVOICE_FOR_ADDRESS_LINE_TWO, settings.ADDRESS_LINE_TWO)
        self.worksheet.update(
            self.INVOICE_FOR_ADDRESS_LINE_THREE, settings.ADDRESS_LINE_THREE)
    
    def add_submission_date(self):
        """Add submission date

        Add today's date as the date of submission
        """
        self.worksheet.update(self.SUBMISSION_DATE, "Submitted on: {}".format(
            self.invoicing_date))
    
    def add_due_date(self):
        """Add the due date

        The due date for the invoice will be 30 days after the submission date
        """
        self.worksheet.update(self.DUE_DATE_TITLE, "Due Date")
        self.worksheet.update(self.DUE_DATE, self.due_date.strftime("%d/%m/%Y"))
    
    def add_additional_titles_to_header(self):
        """Add additional titles to the invoicer header

        Add the remainder of the information to the header of the invoice
        """
        self.worksheet.update(self.TITLE, "Invoice")
        self.worksheet.update(self.PAYABLE_TO_TITLE, "Payable To")
        self.worksheet.update(self.PAYABLE_TO, settings.FULL_NAME)

        self.worksheet.update(self.INVOICE_NUMBER_TITLE, "Invoice #")
        self.worksheet.update(self.PROJECT_TITLE, "Project")
    
    def add_table_headers(self):
        """Add header tables

        Add the headers to the session table
        """
        self.worksheet.update(self.DESCRIPTION_HEADER, "Description")
        self.worksheet.update(self.RATE_HEADER, "Rate")
        self.worksheet.update(self.HOURS_HEADER, "Hours")
        self.worksheet.update(self.TOTAL_HEADER, "Total")
    
    def write_formulas_to_invoice(self):
        """Write formulas to the invoice

        Iterate over the entries in the data recieved from the API and write
        the formulas to the Sheet
        """
        row = self.TABLE_FIRST_ROW

        for entry in self.invoice_data:
            self.worksheet.update_acell(
                self.TABLE_START_COLUMN + row, entry["formula"])
            
            row = str(int(row) + 1)
