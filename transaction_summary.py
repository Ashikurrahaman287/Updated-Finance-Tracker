from telegram import Update
from telegram.ext import CallbackContext
from data.database import get_transactions_for_period
from utils.helpers import format_currency, get_date_n_days_ago, get_today_date

def show_summary(update: Update, context: CallbackContext, days: int, period_name: str) -> None:
    try:
        end_date = get_today_date()
        start_date = get_date_n_days_ago(days)
        transactions = get_transactions_for_period(start_date, end_date)
        summary_text = generate_summary(transactions, period_name)
        update.message.reply_text(summary_text)
    except Exception as e:
        update.message.reply_text(f"An error occurred while fetching the {period_name.lower()} summary: {e}")

def today_summary(update: Update, context: CallbackContext) -> None:
    show_summary(update, context, 0, "Today's")

def last_7_days_summary(update: Update, context: CallbackContext) -> None:
    show_summary(update, context, 7, "Last 7 Days'")

def last_30_days_summary(update: Update, context: CallbackContext) -> None:
    show_summary(update, context, 30, "Last 30 Days'")

def generate_summary(transactions, period_name):
    if not transactions:
        return f"No transactions found for {period_name.lower()}."

    total_debits = 0
    total_credits = 0
    summary_text = f"{period_name} Summary\n\n"

    for transaction in transactions:
        amount = transaction['amount']
        category = transaction['category']
        t_type = transaction['type']
        date = transaction['date']

        if t_type == 'debit':
            total_debits += amount
            summary_text += f"Debit: {format_currency(amount)} - {category} on {date}\n"
        else:
            total_credits += amount
            summary_text += f"Credit: {format_currency(amount)} - {category} on {date}\n"

    summary_text += f"\nTotal Debits: {format_currency(total_debits)}"
    summary_text += f"\nTotal Credits: {format_currency(total_credits)}"
    summary_text += f"\nNet Balance: {format_currency(total_credits - total_debits)}"

    return summary_text
