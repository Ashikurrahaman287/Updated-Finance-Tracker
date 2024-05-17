from telegram import Update
from telegram.ext import CallbackContext
from data.database import get_transactions_for_month
from utils.helpers import format_currency, get_current_month


def monthly_report(update: Update, context: CallbackContext) -> None:
    try:
        # Get the current month and year
        month, year = get_current_month()

        # Retrieve transactions for the current month
        transactions = get_transactions_for_month(month, year)

        if not transactions:
            update.message.reply_text("No transactions found for this month.")
            return

        # Generate the report text
        report_text = f"Monthly Report for {month}/{year}\n\n"
        total_debits = 0
        total_credits = 0

        for transaction in transactions:
            amount = transaction['amount']
            category = transaction['category']
            t_type = transaction['type']
            date = transaction['date']

            if t_type == 'debit':
                total_debits += amount
                report_text += f"Debit: {format_currency(amount)} - {category} on {date}\n"
            else:
                total_credits += amount
                report_text += f"Credit: {format_currency(amount)} - {category} on {date}\n"

        report_text += f"\nTotal Debits: {format_currency(total_debits)}"
        report_text += f"\nTotal Credits: {format_currency(total_credits)}"
        report_text += f"\nNet Balance: {format_currency(total_credits - total_debits)}"

        # Send the report to the user
        update.message.reply_text(report_text)

    except Exception as e:
        update.message.reply_text(f"An error occurred while generating the report: {e}")
