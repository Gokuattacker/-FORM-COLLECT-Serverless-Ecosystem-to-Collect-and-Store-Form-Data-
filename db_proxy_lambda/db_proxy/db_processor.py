import json
import logging
from services.database_service import database_insert, database_table_select_all_values
from services.s3_service import upload_file_to_s3
from models.response import DbProxyBaseResponse, DbProxySelectResponse
from models.response_status import ResponseStatus

from models.db_form_enum import DbFormEnum
from models.db_form_functions_enum import DbFunctionEnum


class DbProcessor():
    def process_event(self, event):
        try: 
            if event[DbFormEnum.FORM_FLAG.value] == DbFunctionEnum.TABLE_INSERT.value:
                database_insert(event[DbFormEnum.FORM_TABLE.value], event[DbFormEnum.FORM_ATTRIBUTE_VALUES.value])
                return DbProxyBaseResponse(ResponseStatus.SUCCESS.value).data
                
            elif event[DbFormEnum.FORM_FLAG.value] == DbFunctionEnum.TABLE_SELECT_ALL.value:
                database_table_select_all_values(event[DbFormEnum.FORM_TABLE.value])
                object_name = upload_file_to_s3("/data/google_sheet_data.csv")

                if(object_name != None):
                    return DbProxySelectResponse(ResponseStatus.SUCCESS.value, object_name).data
                else:
                    return DbProxyBaseResponse(ResponseStatus.FAILURE.value, "Something went wrong").data
            else:
                raise Exception("Invalid Db function Called")

        except Exception as e:
            return DbProxyBaseResponse(ResponseStatus.FAILURE.value, str(e)).data
