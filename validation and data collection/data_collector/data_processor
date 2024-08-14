import json
import logging
from services.db_proxy_service import db_proxy_insert_service
from functions import correct_using_flag_list

class AtlanDataCollector():
    
    def process_event(self, event):
        try:
            for sqs_records in event["Records"]:
                self.__collect_data(json.loads(sqs_records["body"]))
        except Exception as e:
            logging.error(e)
    

    def __collect_data(self, record_body):
        flag_list = record_body["flag_list"]

        form_common_attributes = json.loads(record_body["form_common_attributes"])
        form_specific_attributes = json.loads(record_body["form_specific_attributes"])

        form_specific_attributes = correct_using_flag_list(flag_list, form_specific_attributes)
        form_list = self.__get_list_from_form_attributes(form_common_attributes, form_specific_attributes)
        db_proxy_insert_service(form_list)
        
    
    def __get_list_from_form_attributes(self, form_common_attributes, form_specific_attributes):
        form_list = []

        for key in form_common_attributes:
            form_list.append(form_common_attributes[key])

        for key in form_specific_attributes:
            form_list.append(form_specific_attributes[key])
        
        return form_list


