def format_currency(amount):
    """Format the given amount as currency."""
    return f"${amount:.2f}"

def calculate_total(transactions):
    """Calculate the total amount from a list of transactions."""
    return sum(transaction['amount'] for transaction in transactions)
