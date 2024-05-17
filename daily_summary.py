from telegram.ext import CallbackContext
from data.database import fetch_transactions
from utils.helpers import format_currency, calculate_total

def send_daily_summary(context: CallbackContext):
    chat_id = context.job.context
    summary = generate_daily_summary()
    context.bot.send_message(chat_id=chat_id, text=summary)

def generate_daily_summary():
    transactions = fetch_transactions(limit=10)  # Fetch last 10 transactions for today
    total_debits = calculate_total([t for t in transactions if t['type'] == 'debit'])
    total_credits = calculate_total([t for t in transactions if t['type'] == 'credit'])
    summary = f"Today's Summary:\n"
    summary += f"Total Debits: {format_currency(total_debits)}\n"
    summary += f"Total Credits: {format_currency(total_credits)}\n"
    summary += "Recent Transactions:\n"
    for transaction in transactions:
        summary += f"{transaction['type'].capitalize()} {format_currency(transaction['amount'])} in {transaction['category']}\n"
    return summary
