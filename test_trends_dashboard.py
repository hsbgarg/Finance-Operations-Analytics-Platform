from utils.data_loader import *
from utils.finance_engine import *

transactions = load_transactions()

print(monthly_income_trend(transactions).head())

print(monthly_expense_trend(transactions).head())

print(monthly_transactions(transactions).head())

print(program_trend(transactions).head())