def format_currency(value):
    """
    Format currency using Indian numbering system.
    """

    value = float(value)

    if abs(value) >= 1_00_00_00_000:      # 100 Crore
        return f"₹{value/1_00_00_00_000:.2f} B"

    elif abs(value) >= 1_00_00_000:       # 1 Crore
        return f"₹{value/1_00_00_000:.2f} Cr"

    elif abs(value) >= 1_00_000:          # 1 Lakh
        return f"₹{value/1_00_000:.2f} L"

    else:
        return f"₹{value:,.0f}"

def format_percentage(value):
    return f"{value:.2f}%"

def format_number(value):
    return f"{value:,}"