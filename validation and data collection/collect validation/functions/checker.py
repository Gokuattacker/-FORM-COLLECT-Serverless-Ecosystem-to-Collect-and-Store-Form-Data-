from models.form_response_enum import FormCommonEnum, FormSpecificEnum

"""
Function to run null checks for the parameters
that every form must have.
"""
def null_system_checks(request_body):
    for items in FormCommonEnum:
        if len(request_body[items.value]) == 0:
            raise KeyError('Please contact the owner of the form regarding this issue')
        
"""
Function to run null checks on
the respondent parameters which 
is required to be filled.
"""
def null_respondent_checks(request_body):
    for items in FormSpecificEnum:
        if len(request_body[items.value]) == 0:
            raise KeyError('Some of the required values are missing from the form response')
