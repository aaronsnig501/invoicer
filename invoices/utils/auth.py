"""auth.py

A wrapper over Googles authentication.
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings


def authenticate():
    """Authenticates against Google

    This function wraps up the authentication for the Google API. This will
    allow programmatic access to Google Sheets and Google Drive. The creds are
    read from the `CREDS_LOCATION` setting.

    Returns:
        client (Client): A client object that will be used to communicate with
        the API provided by `gspread`
    """
    scopes = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        settings.CREDS_LOCATION, scopes)
    client = gspread.authorize(credentials)
    return client