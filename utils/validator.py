import pandas as pd

def check_missing_values(df):
    """
    Returns the number of missing values in each column.
    """

    return df.isnull().sum()
def check_duplicate_transactions(df):
    """
    Returns duplicate Transaction IDs.
    """

    return df[df["Transaction_ID"].duplicated()]

def check_expense_amounts(df):
    """
    Expense transactions should always be negative.
    """

    invalid = df[
        (df["Type"] == "Expense") &
        (df["Amount"] > 0)
    ]

    return invalid

def check_income_amounts(df):
    """
    Income transactions should always be positive.
    """

    invalid = df[
        (df["Type"] == "Income") &
        (df["Amount"] < 0)
    ]

    return invalid

def validate_salary_employee(df):
    """
    Salary transactions must have an Employee_ID.
    """

    invalid = df[
        (df["Category"] == "Salary") &
        (df["Employee_ID"].isna())
    ]

    return invalid

def validate_vendor_transactions(df):
    """
    Vendor-based expenses must have a Vendor_ID.
    """

    vendor_categories = [
        "Medicines",
        "Nutrition Kits",
        "Office Supplies",
        "IT Equipment",
        "Consulting"
    ]

    invalid = df[
        (df["Category"].isin(vendor_categories)) &
        (df["Vendor_ID"].isna())
    ]

    return invalid

def validate_program_ids(transactions, programs):
    """
    Every Program_ID in transactions must exist in programs.csv.
    """

    invalid = transactions[
        ~transactions["Program_ID"].isin(programs["Program_ID"])
    ]

    return invalid

def validate_grant_ids(transactions, grants):
    """
    Every Grant_ID in transactions must exist in grants.csv.
    """

    invalid = transactions[
        ~transactions["Grant_ID"].isin(grants["Grant_ID"])
    ]

    return invalid

def generate_validation_report(transactions, programs, grants):
    """
    Runs all validation checks and returns a summary DataFrame.
    """

    report = []

    checks = {

        "Duplicate Transactions":
            check_duplicate_transactions(transactions),

        "Expense Amount Validation":
            check_expense_amounts(transactions),

        "Income Amount Validation":
            check_income_amounts(transactions),

        "Salary Validation":
            validate_salary_employee(transactions),

        "Vendor Validation":
            validate_vendor_transactions(transactions),

        "Program Validation":
            validate_program_ids(transactions, programs),

        "Grant Validation":
            validate_grant_ids(transactions, grants),

        "Payment Method Validation":
            validate_payment_method(transactions),

        "Transaction Type Validation":
            validate_transaction_type(transactions),

        "Status Validation":
            validate_status(transactions),

        "Date Validation":
            validate_dates(transactions)

    }

    for check_name, result in checks.items():

        failed_records = len(result)

        status = "PASS" if failed_records == 0 else "FAIL"

        report.append({
            "Validation Check": check_name,
            "Status": status,
            "Failed Records": failed_records
        })

    return pd.DataFrame(report)

def check_duplicate_employees(employees):
    """
    Duplicate Employee IDs.
    """

    return employees[
        employees["Employee_ID"].duplicated()
    ]

def check_duplicate_vendors(vendors):
    """
    Duplicate Vendor IDs.
    """

    return vendors[
        vendors["Vendor_ID"].duplicated()
    ]
def check_duplicate_programs(programs):
    """
    Duplicate Program IDs.
    """

    return programs[
        programs["Program_ID"].duplicated()
    ]

def validate_payment_method(df):

    valid = [
        "UPI",
        "NEFT",
        "RTGS",
        "Cheque",
        "Bank Transfer"
    ]

    return df[
        ~df["Payment_Method"].isin(valid)
    ]

def validate_transaction_type(df):

    return df[
        ~df["Type"].isin(
            ["Income", "Expense"]
        )
    ]

def validate_status(df):

    valid = [
        "Completed",
        "Pending",
        "Failed"
    ]

    return df[
        ~df["Status"].isin(valid)
    ]

def validate_dates(df):

    invalid = df.copy()

    invalid["Date"] = pd.to_datetime(
        invalid["Date"],
        errors="coerce"
    )

    return invalid[
        invalid["Date"].isna()
    ]

