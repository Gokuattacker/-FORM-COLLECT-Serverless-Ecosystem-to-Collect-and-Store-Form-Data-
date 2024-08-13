from models.data_model import DataModel
from models.form_response_enum import FormSpecificEnum


class FormSpecificModel(DataModel):
    def __init__(self, name, email, mobile_no, gender, age, total_income, total_savings, total_expenditure, food_expenditure, cable_expenditure, healthcare_expenditure, fuel_expenditure):
        self.name = name
        self.email = email
        self.mobile_no = mobile_no
        self.gender = gender
        self.age = age
        self.total_income = total_income    
        self.total_savings = total_savings  
        self.total_expenditure = total_expenditure  
        self.food_expenditure = food_expenditure  
        self.cable_expenditure = cable_expenditure  
        self.healthcare_expenditure = healthcare_expenditure  
        self.fuel_expenditure = fuel_expenditure  

    @property
    def data(self):
        return {
            FormSpecificEnum.NAME.value: self.name,
            FormSpecificEnum.EMAIL.value: self.email,
            FormSpecificEnum.MOBILE_NUMBER.value: self.mobile_no,
            FormSpecificEnum.GENDER.value: self.gender,
            FormSpecificEnum.AGE.value: self.age,
            FormSpecificEnum.MONTHLY_INCOME.value: self.total_income,
            FormSpecificEnum.MONTHLY_TOTAL_EXPENDITURE.value: self.total_expenditure,
            FormSpecificEnum.MONTHLY_SAVINGS.value: self.total_savings,
            FormSpecificEnum.MONTHLY_CABLE_EXPENDITURE.value: self.cable_expenditure,
            FormSpecificEnum.MONTHLY_FOOD_EXPENDITURE.value: self.food_expenditure,
            FormSpecificEnum.MONTHLY_HEALTHCARE_EXPENDITURE.value: self.healthcare_expenditure,
            FormSpecificEnum.MONTHLY_FUEL_EXPENDITURE.value: self.fuel_expenditure,
        }
    
    def get_total_income(self):
        return self.total_income
     
    def get_total_expenditure(self):
        return self.total_expenditure
        
    def get_total_savings(self):
        return self.total_savings

    def get_cable_expenditure(self):
        return self.cable_expenditure
    
    def get_food_expenditure(self):
        return self.food_expenditure
    
    def get_healthcare_expenditure(self):
        return self.healthcare_expenditure
    
    def get_fuel_expenditure(self):
        return self.fuel_expenditure
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__



        

