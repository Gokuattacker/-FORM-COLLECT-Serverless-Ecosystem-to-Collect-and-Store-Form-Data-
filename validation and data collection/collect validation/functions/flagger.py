
def check_monthly_income_and_savings(total_income, total_savings, total_expenditure):
    calculated_monthly_savings = (total_income-total_expenditure)
    
    if total_savings >= calculated_monthly_savings:
        return True
        
    return False

def check_monthly_expenditure_with_sum_of_individual_expenses(
    total_expenditure, food_expenditure, cable_expenditure, healthcare_expenditure, fuel_expenditure):
    calculated_total_expenditure = food_expenditure + cable_expenditure + healthcare_expenditure + fuel_expenditure

    if calculated_total_expenditure >= total_expenditure:
        return True
    
    return False
    

