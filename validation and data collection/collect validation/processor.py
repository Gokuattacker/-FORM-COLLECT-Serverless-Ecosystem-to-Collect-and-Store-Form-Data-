import sys
from functions.checker import null_respondent_checks, null_system_checks

from models.response import ValidationApiResponse
from models.response_status import ResponseStatus
from functions.flagger import check_monthly_expenditure_with_sum_of_individual_expenses, check_monthly_income_and_savings
from models.form_common_model import FormCommonModel
from models.form_response_enum import FormCommonEnum, FormSpecificEnum
from models.form_specific_model import FormSpecificModel
from models.form_sqs_model import FormSQSModel
from services.sqs_service import send_message_to_sqs_service

class ValidationProcessor():
    
    def __init__(self, request_body):
        self.request_body = request_body

    def process_event(self):
        try:
            null_system_checks(self.request_body)
            null_respondent_checks(self.request_body)
            
            form_common_model = FormCommonModel(
                self.request_body[FormCommonEnum.RESPONSE_ID.value],
                self.request_body[FormCommonEnum.RESPONSE_FAMILY_ID.value],
                self.request_body[FormCommonEnum.USER_ID.value],
                self.request_body[FormCommonEnum.USERNAME.value],
                self.request_body[FormCommonEnum.LOCATION.value],
                self.request_body[FormCommonEnum.SUBMITTED_TIME.value],
                self.request_body[FormCommonEnum.SYNCED_TIME.value],
                self.request_body[FormCommonEnum.LAST_MODIFIED_TIME.value]
            )

            form_specific_model = FormSpecificModel(
                self.request_body[FormSpecificEnum.NAME.value],
                self.request_body[FormSpecificEnum.EMAIL.value],
                self.request_body[FormSpecificEnum.MOBILE_NUMBER.value],
                self.request_body[FormSpecificEnum.GENDER.value],
                int(self.request_body[FormSpecificEnum.AGE.value]),
                float(self.request_body[FormSpecificEnum.MONTHLY_INCOME.value]),
                float(self.request_body[FormSpecificEnum.MONTHLY_SAVINGS.value]),
                float(self.request_body[FormSpecificEnum.MONTHLY_TOTAL_EXPENDITURE.value]),
                float(self.request_body[FormSpecificEnum.MONTHLY_FOOD_EXPENDITURE.value]),
                float(self.request_body[FormSpecificEnum.MONTHLY_CABLE_EXPENDITURE.value]),
                float(self.request_body[FormSpecificEnum.MONTHLY_HEALTHCARE_EXPENDITURE.value]),
                float(self.request_body[FormSpecificEnum.MONTHLY_FUEL_EXPENDITURE.value])
            )

            flag_list = self.__flag_events(form_specific_model)

            form_sqs_model = FormSQSModel(form_common_model, form_specific_model, flag_list)
            send_message_to_sqs_service(form_sqs_model.get_message_body())

            return ValidationApiResponse(ResponseStatus.SUCCESS.value, "Form Successfully Submitted").data
        except KeyError as err:
            err_value = sys.exc_info()
            return ValidationApiResponse(ResponseStatus.FAILURE.value, str(err_value)).data
        except Exception as e:
            err_value = sys.exc_info()
            return ValidationApiResponse(ResponseStatus.INTERNAL_ERROR.value, str(err_value)).data
    
    def __flag_events(self, form_specific_model):
        flag_list = []
        total_income = form_specific_model.get_total_income()
        total_savings = form_specific_model.get_total_savings()
        total_expenditure = form_specific_model.get_total_expenditure()
        food_expenditure = form_specific_model.get_food_expenditure()
        cable_expenditure = form_specific_model.get_cable_expenditure()
        healthcare_expenditure = form_specific_model.get_healthcare_expenditure()
        fuel_expenditure = form_specific_model.get_fuel_expenditure()

        if check_monthly_expenditure_with_sum_of_individual_expenses(total_expenditure, food_expenditure, cable_expenditure, healthcare_expenditure, fuel_expenditure):
            flag_list.append("Rule1")
            total_expenditure = (food_expenditure + cable_expenditure + healthcare_expenditure + fuel_expenditure)
        
        if check_monthly_income_and_savings(total_income, total_savings, total_expenditure):
            flag_list.append("Rule2")  

        return flag_list      
