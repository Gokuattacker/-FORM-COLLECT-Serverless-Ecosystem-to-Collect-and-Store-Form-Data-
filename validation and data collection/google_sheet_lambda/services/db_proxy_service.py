import json
import logging
import os
from models.response_status import ResponseStatus
from models.db_form_enum import DbFormEnum
import boto3

def db_proxy_get_all_values(table_name):
    db_lambda_client = boto3.client('lambda')
    try:
        lambda_event = {
            DbFormEnum.FORM_FLAG.value: "SelectAll",
            DbFormEnum.FORM_TABLE.value: "collectForm"
        }

        db_proxy_function_arn = os.environ.get("DB_PROXY_ARN")

        response = db_lambda_client.invoke(
            FunctionName = db_proxy_function_arn,
            InvocationType = "RequestResponse",
            Payload = json.dumps(lambda_event)
        )

        response_dict = json.load(response['Payload'])            
        if response_dict["status"] == ResponseStatus.SUCCESS.value:
            return response_dict["object_name"]
        else:
            return None
    except Exception as e:
        logging.error(e)
        return None

