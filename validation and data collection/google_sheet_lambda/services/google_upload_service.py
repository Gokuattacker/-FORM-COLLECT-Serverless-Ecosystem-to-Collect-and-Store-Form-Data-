from services.s3_service import get_google_credentials_from_s3
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def import_data_to_google_sheets(csv_content, table_name):
    try:
        credentials_json_file = get_google_credentials_from_s3()
        if credentials_json_file == None:
            raise Exception("Credentials not found")

        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', 
        "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_json_file, scope)
        client = gspread.authorize(credentials)
        google_sheet_name = f'Atlan-Collect-{table_name}'
        spreadsheet = client.open(google_sheet_name)

        client.import_csv(spreadsheet.id, data=csv_content)
        return google_sheet_name
    except Exception as e:
        print(e)
        raise e