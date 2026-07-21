import pandas as pd
import numpy as np
import random
import os

from faker import Faker

fake = Faker("en_IN")

os.makedirs("data", exist_ok=True)

states = [
    "Maharashtra",
    "Gujarat",
    "Karnataka",
    "Tamil Nadu",
    "Delhi",
    "Rajasthan",
    "Uttar Pradesh",
    "Madhya Pradesh"
]
departments = [
    "Finance",
    "Operations",
    "Programs",
    "HR",
    "IT",
    "Procurement",
    "Administration"
]
designations = [
    "Analyst",
    "Associate",
    "Manager",
    "Senior Manager",
    "Coordinator",
    "Executive",
    "Officer"
]
program_names = [
    "Child Nutrition",
    "Maternal Health",
    "School Meals",
    "Rural Healthcare",
    "Anaemia Prevention",
    "Health Awareness",
    "Mobile Clinics",
    "Immunization",
    "Women's Health",
    "Mental Health",
    "Medical Camps",
    "Community Outreach",
    "Water & Sanitation",
    "Emergency Relief",
    "Nutrition Education"
]

vendor_categories = [
    "Medicines",
    "Nutrition Kits",
    "Transport",
    "Office Supplies",
    "IT Equipment",
    "Training",
    "Consulting",
    "Utilities"
]
payment_terms = [
    "Immediate",
    "15 Days",
    "30 Days",
    "45 Days"
]

donors = [

    "UNICEF",
    "WHO",
    "Bill & Melinda Gates Foundation",
    "Infosys Foundation",
    "Tata Trusts",
    "Government of India",
    "Reliance Foundation",
    "CSR Partnership",
    "Azim Premji Foundation",
    "HDFC CSR"

]
budget_departments = [

    "Programs",
    "Operations",
    "Healthcare",
    "Nutrition",
    "Administration"

]

expense_categories = [
    "Salary",
    "Medicines",
    "Nutrition Kits",
    "Travel",
    "Rent",
    "Utilities",
    "Training",
    "Office Supplies",
    "IT Equipment",
    "Consulting"
]

income_categories = [
    "Government Grant",
    "CSR Grant",
    "International NGO",
    "Individual Donation",
    "Corporate Donation"
]

payment_methods = [
    "Bank Transfer",
    "NEFT",
    "RTGS",
    "UPI",
    "Cheque"
]

transaction_status = [
    "Completed",
    "Completed",
    "Completed",
    "Completed",
    "Pending",
    "Failed"
]

expense_amount_ranges = {

    "Salary": (30000, 150000),

    "Medicines": (50000, 500000),

    "Nutrition Kits": (20000, 400000),

    "Travel": (2000, 50000),

    "Rent": (50000, 200000),

    "Utilities": (5000, 75000),

    "Training": (10000, 100000),

    "Office Supplies": (5000, 50000),

    "IT Equipment": (50000, 500000),

    "Consulting": (50000, 300000)

}

expense_weights = {

    "Salary": 35,

    "Medicines": 20,

    "Nutrition Kits": 15,

    "Travel": 8,

    "Rent": 5,

    "Utilities": 4,

    "Training": 4,

    "Office Supplies": 3,

    "IT Equipment": 3,

    "Consulting": 3

}

income_weights = {

    "Government Grant": 40,

    "CSR Grant": 25,

    "International NGO": 20,

    "Corporate Donation": 10,

    "Individual Donation": 5

}



income_amount_ranges = {

    "Government Grant": (1000000, 50000000),

    "CSR Grant": (500000, 20000000),

    "International NGO": (1000000, 30000000),

    "Corporate Donation": (100000, 5000000),

    "Individual Donation": (1000, 100000)

}

employees = []

for i in range(1,301):

    employees.append({

        "Employee_ID": f"E{i:03}",

        "Name": fake.name(),

        "Department": random.choice(departments),

        "Designation": random.choice(designations),

        "State": random.choice(states),

        "Salary": random.randint(30000,150000),

        "Joining_Date": fake.date_between(
            start_date="-8y",
            end_date="today"
        ),

        "Email": fake.email()

    })

employees_df = pd.DataFrame(employees)

employees_df.to_csv(
"data/employees.csv",
index=False
)

#geerate vendors
vendors = []

for i in range(1,121):

    vendors.append({

        "Vendor_ID": f"V{i:03}",

        "Vendor_Name": fake.company(),

        "Category": random.choice(vendor_categories),

        "State": random.choice(states),

        "Payment_Terms": random.choice(payment_terms),

        "GST_Number": fake.bothify("27ABCDE####F1Z5")

    })

vendors_df = pd.DataFrame(vendors)

vendors_df.to_csv(
    "data/vendors.csv",
    index=False
)

#generate programs

programs = []

for i, program in enumerate(program_names, start=1):

    programs.append({

        "Program_ID": f"P{i:03}",

        "Program_Name": program,

        "State": random.choice(states),

        "Manager": fake.name(),

        "Beneficiaries": random.randint(500,10000),

        "Start_Date": fake.date_between(
            start_date="-5y",
            end_date="-1y"
        ),

        "End_Date": fake.date_between(
            start_date="+6m",
            end_date="+3y"
        )

    })
    

programs_df = pd.DataFrame(programs)

grants = []

for i in range(1,26):

    grant_amount = random.randint(5000000,50000000)

    grants.append({

        "Grant_ID": f"G{i:03}",

        "Donor": random.choice(donors),

        "Program_ID": random.choice(programs_df["Program_ID"]),

        "Grant_Amount": grant_amount,

        "Start_Date": fake.date_between(
            start_date="-2y",
            end_date="-6m"
        ),

        "End_Date": fake.date_between(
            start_date="+6m",
            end_date="+3y"
        )

    })

grants_df = pd.DataFrame(grants)

grants_df.to_csv(
    "data/grants.csv",
    index=False
)

budget = []

for program in programs_df["Program_ID"]:

    budget.append({

        "Program_ID": program,

        "Year": 2026,

        "Department": random.choice(budget_departments),

        "Budget_Amount": random.randint(
            10000000,
            60000000
        )

    })

budget_df = pd.DataFrame(budget)

budget_df.to_csv(
    "data/budget.csv",
    index=False
)

transactions = []
for i in range(1, 20001):

    transaction_type = random.choice(["Income", "Expense"])

    transactions = []

for i in range(1, 20001):

    transaction_type = random.choice(["Income", "Expense"])

    if transaction_type == "Income":

        category = random.choices(

            list(income_weights.keys()),

            weights=list(income_weights.values()),

            k=1

        )[0]
        
        low, high = income_amount_ranges[category]
        amount = random.randint(low, high)

        vendor = None
        employee = None
        grant = random.choice(grants_df["Grant_ID"])
        description = category

    else:

        category = random.choices(

            list(expense_weights.keys()),

            weights=list(expense_weights.values()),

            k=1

        )[0]

        low, high = expense_amount_ranges[category]
        amount = -random.randint(low, high)

        grant = random.choice(grants_df["Grant_ID"])
        description = category

        if category == "Salary":
            employee = random.choice(employees_df["Employee_ID"])
            vendor = None
        else:
            vendor = random.choice(vendors_df["Vendor_ID"])
            employee = None

    transactions.append({   

        "Transaction_ID": f"T{i:06}",
        "Date": fake.date_between(start_date="-2y", end_date="today"),
        "Type": transaction_type,
        "Category": category,
        "Amount": amount,
        "Vendor_ID": vendor,
        "Employee_ID": employee,
        "Program_ID": random.choice(programs_df["Program_ID"]),
        "Grant_ID": grant,
        "State": random.choice(states),
        "Payment_Method": random.choice(payment_methods),
        "Status": random.choice(transaction_status),
        "Description": description

    })

transactions_df = pd.DataFrame(transactions)

transactions_df.to_csv(
    "data/transactions.csv",
    index=False
)

print("Transactions :", len(transactions_df))


programs_df.to_csv(
    "data/programs.csv",
    index=False
)

print("Master datasets created successfully!")

print()

print("Employees :", len(employees_df))

print("Vendors :", len(vendors_df))

print("Programs :", len(programs_df))
print("Grants :", len(grants_df))
print("Budgets :", len(budget_df))


