from services.google_upload_service import import_data_to_google_sheets
from services.s3_service import delete_csv_from_s3, get_csv_from_s3
from services.db_proxy_service import db_proxy_get_all_values
from models.response import GoogleSheetApiResponse
from models.response_status import ResponseStatus


class GoogleSheetProcessor():
    def __init__(self, request_body):
        self.request_body = request_body
    

    def process_event(self):
        try:
            object_name = db_proxy_get_all_values(self.request_body["table_name"])
            if object_name == None:
                raise Exception

            csv_content=get_csv_from_s3(object_name)
            if csv_content == None:
                raise Exception

            response = delete_csv_from_s3(object_name)
            if response == None:
                raise Exception
            
            google_sheet_name=import_data_to_google_sheets(csv_content, self.request_body["table_name"])
            return GoogleSheetApiResponse(ResponseStatus.SUCCESS.value, "Success!", google_sheet_name).data

        except Exception as e:
            return GoogleSheetApiResponse(ResponseStatus.FAILURE.value, "Something Went Wrong").data