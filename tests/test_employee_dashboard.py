from utils.data_loader import *
from utils.finance_engine import *

transactions = load_transactions()
employees = load_employees()

print(salary_by_department(transactions, employees))
print(employee_state_distribution(employees))
print(designation_distribution(employees))
print(monthly_salary(transactions))
print(payroll_cost(transactions))
print(average_salary(employees))
print(highest_salary(employees))
print(employee_table(employees).head())