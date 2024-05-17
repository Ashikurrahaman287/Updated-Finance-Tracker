from telegram import Update
from telegram.ext import CallbackContext
from data.database import add_transaction_to_db

def add_debit(update: Update, context: CallbackContext) -> None:
    try:
        amount = float(context.args[0])
        category = context.args[1] if len(context.args) > 1 else "General"
        add_transaction_to_db("debit", amount, category)
        update.message.reply_text(f"Debit of {amount} added to {category}.")
    except (IndexError, ValueError):
        update.message.reply_text("Usage: /Debt <amount> [category]")

def add_credit(update: Update, context: CallbackContext) -> None:
    try:
        amount = float(context.args[0])
        category = context.args[1] if len(context.args) > 1 else "General"
        add_transaction_to_db("credit", amount, category)
        update.message.reply_text(f"Credit of {amount} added to {category}.")
    except (IndexError, ValueError):
        update.message.reply_text("Usage: /Crd <amount> [category]")
