from utils.data_loader import *
from utils.validator import *

transactions = load_transactions()
programs = load_programs()
grants = load_grants()

print("Salary Validation")
print(validate_salary_employee(transactions))

print()

print("Vendor Validation")
print(validate_vendor_transactions(transactions))

print()

print("Program Validation")
print(validate_program_ids(transactions, programs))

print()

print("Grant Validation")
print(validate_grant_ids(transactions, grants))