from utils.data_loader import *
from utils.finance_engine import *

transactions = load_transactions()
budget = load_budget()
grants = load_grants()

print("Budget")
print(total_budget(budget))

print()

print("Budget Utilization")
print(budget_utilization(transactions, budget))

print()

print("Budget Remaining")
print(budget_remaining(transactions, budget))

print()

print("Grant Amount")
print(total_grants(grants))

print()

print("Grant Utilization")
print(grant_utilization(transactions, grants))

print()

print("Grant Remaining")
print(grant_remaining(transactions, grants))

print("\nMonthly Income")
print(monthly_income(transactions))

print("\nMonthly Expenses")
print(monthly_expenses(transactions))

print("\nMonthly Cash Flow")
print(monthly_cash_flow(transactions))