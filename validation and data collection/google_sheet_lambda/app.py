import sys

from models.response import GoogleSheetApiResponse
from models.response_status import ResponseStatus
from processor import GoogleSheetProcessor

def lambda_handler(event, context):
    try:
        parsed_event_body_json = event['body']
        google_sheet_processor = GoogleSheetProcessor(parsed_event_body_json)
        return google_sheet_processor.process_event()
    except Exception as e:
        err_value = sys.exc_info()
        return GoogleSheetApiResponse(ResponseStatus.FAILURE.value, "Something Went Wrong").data
