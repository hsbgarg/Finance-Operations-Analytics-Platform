import pandas as pd
def total_income(transactions):
    """
    Calculate total income.
    """

    income = transactions[
        transactions["Type"] == "Income"
    ]["Amount"].sum()

    return income

def total_expenses(transactions):
    """
    Calculate total expenses.
    """

    expenses = transactions[
        transactions["Type"] == "Expense"
    ]["Amount"].sum()

    return abs(expenses)

def net_cash_flow(transactions):
    """
    Income - Expenses
    """

    return total_income(transactions) - total_expenses(transactions)

def total_transactions(transactions):

    return len(transactions)

def total_budget(budget):
    """
    Total approved budget.
    """

    return budget["Budget_Amount"].sum()

def budget_utilization(transactions, budget):
    """
    Budget utilization percentage.
    """

    expenses = total_expenses(transactions)

    approved_budget = total_budget(budget)

    return (expenses / approved_budget) * 100

def budget_remaining(transactions, budget):

    return total_budget(budget) - total_expenses(transactions)

def total_grants(grants):

    return grants["Grant_Amount"].sum()

def grant_utilization(transactions, grants):

    expenses = total_expenses(transactions)

    available = total_grants(grants)

    return (expenses / available) * 100

def grant_remaining(transactions, grants):

    return total_grants(grants) - total_expenses(transactions)

def monthly_income(transactions):
    """
    Monthly income trend.
    """

    df = transactions.copy()

    df["Date"] = pd.to_datetime(df["Date"])

    income = (
        df[df["Type"] == "Income"]
        .groupby(df["Date"].dt.to_period("M"))["Amount"]
        .sum()
        .reset_index()
    )

    income["Date"] = income["Date"].astype(str)

    return income

def monthly_expenses(transactions):
    """
    Monthly expense trend.
    """

    df = transactions.copy()

    df["Date"] = pd.to_datetime(df["Date"])

    expenses = (
        df[df["Type"] == "Expense"]
        .groupby(df["Date"].dt.to_period("M"))["Amount"]
        .sum()
        .abs()
        .reset_index()
    )

    expenses["Date"] = expenses["Date"].astype(str)

    return expenses

def monthly_cash_flow(transactions):
    """
    Net cash flow by month.
    """

    df = transactions.copy()

    df["Date"] = pd.to_datetime(df["Date"])

    cashflow = (
        df.groupby(df["Date"].dt.to_period("M"))["Amount"]
        .sum()
        .reset_index()
    )

    cashflow["Date"] = cashflow["Date"].astype(str)

    return cashflow

def expense_by_category(transactions):

    expenses = transactions[
        transactions["Type"] == "Expense"
    ]

    return (

        expenses.groupby("Category")["Amount"]

        .sum()

        .abs()

        .reset_index()

    )

def top_programs(transactions):

    expenses = transactions[
        transactions["Type"] == "Expense"
    ]

    return (

        expenses.groupby("Program_ID")["Amount"]

        .sum()

        .abs()

        .sort_values(ascending=False)

        .head(10)

        .reset_index()

    )

# ==========================================================
# Budget Dashboard Functions
# ==========================================================

def budget_by_department(budget):

    return (
        budget.groupby("Department")["Budget_Amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )


def actual_by_department(transactions):

    mapping = {

        "Salary": "Administration",

        "Office Supplies": "Administration",

        "IT Equipment": "Administration",

        "Rent": "Operations",

        "Travel": "Operations",

        "Utilities": "Operations",

        "Medicines": "Healthcare",

        "Nutrition Kits": "Nutrition",

        "Consulting": "Programs",

        "Training": "Programs"

    }

    expenses = transactions[
        transactions["Type"] == "Expense"
    ].copy()

    expenses["Department"] = expenses["Category"].map(mapping)

    return (

        expenses.groupby("Department")["Amount"]

        .sum()

        .abs()

        .reset_index()

    )


def budget_vs_actual(transactions, budget):

    budget_df = budget_by_department(budget)

    actual_df = actual_by_department(transactions)

    merged = budget_df.merge(
        actual_df,
        on="Department",
        how="left"
    )

    merged = merged.fillna(0)

    merged.rename(
        columns={
            "Budget_Amount": "Budget",
            "Amount": "Actual"
        },
        inplace=True
    )

    return merged

# ==========================================================
# Vendor Dashboard Functions
# ==========================================================

def vendor_spend(transactions):

    expenses = transactions[
        (transactions["Type"] == "Expense") &
        (transactions["Vendor_ID"].notna())
    ]

    return (
        expenses.groupby("Vendor_ID")["Amount"]
        .sum()
        .abs()
        .sort_values(ascending=False)
        .reset_index()
    )


def top_vendors(transactions, n=10):

    return vendor_spend(transactions).head(n)


def payment_method_breakdown(transactions):

    return (
        transactions.groupby("Payment_Method")["Amount"]
        .count()
        .reset_index(name="Transactions")
    )


def vendor_state_distribution(transactions):

    expenses = transactions[
        transactions["Vendor_ID"].notna()
    ]

    return (
        expenses.groupby("State")["Amount"]
        .sum()
        .abs()
        .reset_index()
    )

def salary_by_department(transactions, employees):

    salary = transactions[
        transactions["Category"] == "Salary"
    ].copy()

    salary = salary.merge(

        employees[
            [
                "Employee_ID",
                "Department"
            ]
        ],

        on="Employee_ID",

        how="left"

    )

    return (

        salary.groupby("Department")["Amount"]

        .sum()

        .abs()

        .reset_index()

    )


def employee_state_distribution(employees):

    return (

        employees.groupby("State")["Employee_ID"]

        .count()

        .reset_index(name="Employees")

    )

def designation_distribution(employees):

    return (

        employees.groupby("Designation")["Employee_ID"]

        .count()

        .reset_index(name="Employees")

    )
def monthly_salary(transactions):

    salary = transactions[
        transactions["Category"] == "Salary"
    ].copy()

    salary["Date"] = pd.to_datetime(salary["Date"])

    monthly = (

        salary.groupby(
            salary["Date"].dt.to_period("M")
        )["Amount"]

        .sum()

        .abs()

        .reset_index()

    )

    monthly["Date"] = monthly["Date"].astype(str)

    return monthly

def payroll_cost(transactions):

    salary = transactions[
        transactions["Category"] == "Salary"
    ]

    return abs(salary["Amount"].sum())

def average_salary(employees):

    return employees["Salary"].mean()

def highest_salary(employees):

    return employees["Salary"].max()


def employee_table(employees):

    return employees[
        [
            "Employee_ID",
            "Name",
            "Department",
            "Designation",
            "State",
            "Salary"
        ]
    ]

def monthly_expense_trend(transactions):

    expense = transactions[
        transactions["Type"] == "Expense"
    ].copy()

    expense["Date"] = pd.to_datetime(expense["Date"])

    return (
        expense
        .groupby(expense["Date"].dt.to_period("M"))["Amount"]
        .sum()
        .abs()
        .reset_index()
        .assign(Date=lambda x: x["Date"].astype(str))
    )

def monthly_income_trend(transactions):

    income = transactions[
        transactions["Type"] == "Income"
    ].copy()

    income["Date"] = pd.to_datetime(income["Date"])

    return (
        income
        .groupby(income["Date"].dt.to_period("M"))["Amount"]
        .sum()
        .reset_index()
        .assign(Date=lambda x: x["Date"].astype(str))
    )

def monthly_transactions(transactions):

    df = transactions.copy()

    df["Date"] = pd.to_datetime(df["Date"])

    return (
        df
        .groupby(df["Date"].dt.to_period("M"))
        .size()
        .reset_index(name="Transactions")
        .assign(Date=lambda x: x["Date"].astype(str))
    )

def program_trend(transactions):

    expense = transactions[
        transactions["Type"] == "Expense"
    ]

    return (
        expense
        .groupby("Program_ID")["Amount"]
        .sum()
        .abs()
        .sort_values(ascending=False)
        .reset_index()
    )



