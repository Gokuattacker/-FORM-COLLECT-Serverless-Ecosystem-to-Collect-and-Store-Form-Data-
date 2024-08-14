import json
import logging
import os
from models.db_form_enum import DbFormEnum
from models.response_status import ResponseStatus
import boto3

db_lambda_client = boto3.client('lambda')

def db_proxy_insert_service(form_list_values):
    try:
        lambda_event = {
            DbFormEnum.FORM_FLAG.value: "Insert",
            DbFormEnum.FORM_TABLE.value: "collectForm",
            DbFormEnum.FORM_ATTRIBUTE_VALUES.value: form_list_values
        }

        db_proxy_function_arn = os.environ.get("DB_PROXY_ARN")

        response = db_lambda_client.invoke(
            FunctionName = db_proxy_function_arn,
            InvocationType = "RequestResponse",
            Payload = json.dumps(lambda_event)
        )

        print(response['Payload'])

        response_dict = json.load(response['Payload'])

        if response_dict["status"] == ResponseStatus.SUCCESS.value:
            logging.info(f"Form data with response_id {form_list_values[0]} added to database")
        else:
            logging.error("Error occured while processing data to database")

    except Exception as e:
        logging.exception(e)