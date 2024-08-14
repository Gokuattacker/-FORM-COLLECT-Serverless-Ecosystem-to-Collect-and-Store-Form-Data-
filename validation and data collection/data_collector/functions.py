from models.form_response_enum import FormCommonEnum, FormSpecificEnum
from models.flag_enum import FlagEnum

def correct_using_flag_list(flag_list, form_specific_attributes):
    for flag in flag_list:
        if flag == FlagEnum.RULE_ONE.value:
            food_expenditure = form_specific_attributes[FormSpecificEnum.MONTHLY_FOOD_EXPENDITURE.value]
            cable_expenditure = form_specific_attributes[FormSpecificEnum.MONTHLY_CABLE_EXPENDITURE.value]
            healthcare_expenditure = form_specific_attributes[FormSpecificEnum.MONTHLY_HEALTHCARE_EXPENDITURE.value]
            fuel_expenditure = form_specific_attributes[FormSpecificEnum.MONTHLY_FUEL_EXPENDITURE.value]

            new_total_expenditure = (food_expenditure + cable_expenditure + healthcare_expenditure + fuel_expenditure)
            form_specific_attributes.update({FormSpecificEnum.MONTHLY_TOTAL_EXPENDITURE.value: new_total_expenditure})

        elif flag == FlagEnum.RULE_TWO.value:
            form_specific_attributes.update({FormSpecificEnum.MONTHLY_SAVINGS.value: 0})
        
    return form_specific_attributes
        
    
