import os.path
from typing import Literal
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pathlib import Path

root = Path(__file__).parent


class GSheetClient:
    def __init__(self, spreadsheet_id, scopes):
        self.spreadsheet_id = spreadsheet_id
        self.scopes = scopes
        self.service = build(
            "sheets", "v4", credentials=self._get_credentials())

    def _get_credentials(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        token_path = root/"token.json"
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(
                token_path, self.scopes)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    root/"google.credentials.json", self.scopes
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(token_path, "w") as token:
                token.write(creds.to_json())

        return creds

    def get_values(self, range_name):
        try:
            sheet = self.service.spreadsheets()
            result = (
                sheet.values()
                .get(spreadsheetId=self.spreadsheet_id, range=range_name)
                .execute()
            )
            rows = result.get("values", [])
            # print(f"{len(rows)} rows retrieved")
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

    def batch_get_values(self, range_names):
        try:
            result = (
                self.service.spreadsheets()
                .values()
                .batchGet(spreadsheetId=self.spreadsheet_id, ranges=range_names)
                .execute()
            )
            ranges = result.get("valueRanges", [])
            # print(f"{len(ranges)} ranges retrieved")
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

    def append_values(self, range_name,  values: list[list], value_input_option: Literal["USER_ENTERED", "RAW"]):
        try:
            body = {"values": values}
            result = (
                self.service.spreadsheets()
                .values()
                .append(
                    spreadsheetId=self.spreadsheet_id,
                    range=range_name,
                    valueInputOption=value_input_option,
                    body=body,
                )
                .execute()
            )
            print(f"{(result.get('updates').get('updatedCells'))} cells appended.")
            return result

        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

    def update_values(self, range_name, values: list[list], value_input_option: Literal["USER_ENTERED", "RAW"]):
        try:
            body = {"values": values}
            result = (
                self.service.spreadsheets()
                .values()
                .update(
                    spreadsheetId=self.spreadsheet_id,
                    range=range_name,
                    valueInputOption=value_input_option,
                    body=body,
                )
                .execute()
            )
            print(f"{result.get('updatedCells')} cells updated.")
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error
