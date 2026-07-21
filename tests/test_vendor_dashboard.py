from utils.data_loader import *
from utils.finance_engine import *

transactions = load_transactions()

print()

print(top_vendors(transactions))

print()

print(payment_method_breakdown(transactions))

print()

print(vendor_state_distribution(transactions))
