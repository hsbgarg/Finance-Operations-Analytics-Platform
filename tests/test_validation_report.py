from utils.data_loader import *
from utils.validator import *

transactions = load_transactions()
programs = load_programs()
grants = load_grants()

report = generate_validation_report(
    transactions,
    programs,
    grants
)

print(report)