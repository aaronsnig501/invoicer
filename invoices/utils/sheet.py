"""sheet.py

Handle the formatting of the Google Sheet
"""
from gspread_formatting  import (
    cellFormat, color, textFormat, format_cell_ranges)


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

    TABLE_HEADER_ROW = "19"
    DESCRIPTION_HEADER = "B" + TABLE_HEADER_ROW
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