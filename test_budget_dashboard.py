from utils.data_loader import *
from utils.finance_engine import *

transactions = load_transactions()
budget = load_budget()

print()

print(budget_by_department(budget))

print()

print(actual_by_department(transactions))

print()

print(budget_vs_actual(transactions, budget))