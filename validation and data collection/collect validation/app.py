import sys
from models.response import ValidationApiResponse
from models.response_status import ResponseStatus
from processor import ValidationProcessor


def lambda_handler(event, context):
    try:
        parsed_event_body_json = event['body']
        validation_processor = ValidationProcessor(parsed_event_body_json)
        return validation_processor.process_event()
    except Exception as e:
        err_value = sys.exc_info()
        return ValidationApiResponse(ResponseStatus.FAILURE.value, str(err_value)).data

