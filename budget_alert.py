from telegram.ext import CallbackContext
from data.database import fetch_budget, fetch_transactions
from utils.helpers import format_currency, calculate_total

def send_budget_alert(context: CallbackContext):
    chat_id = context.job.context
    alert_message = generate_budget_alert()
    if alert_message:
        context.bot.send_message(chat_id=chat_id, text=alert_message)

def generate_budget_alert():
    categories = ['Groceries', 'Utilities', 'Entertainment']  # Example categories to monitor
    alert_message = ""
    for category in categories:
        budget = fetch_budget(category)
        if budget:
            transactions = fetch_transactions()  # Fetch all transactions for the category
            total_spent = calculate_total([t for t in transactions if t['category'] == category and t['type'] == 'debit'])
            if total_spent > budget:
                alert_message += f"You have exceeded the budget for {category}. Budget: {format_currency(budget)}, Total Spent: {format_currency(total_spent)}\n"
    return alert_message
