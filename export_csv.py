import csv
import os
from telegram import Update
from telegram.ext import CallbackContext
from data.database import get_all_transactions
from utils.helpers import get_csv_file_path


def export_csv(update: Update, context: CallbackContext) -> None:
    try:
        # Retrieve all transactions from the database
        transactions = get_all_transactions()

        # Get the file path for the CSV file
        csv_file_path = get_csv_file_path()

        # Write transactions to the CSV file
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Type', 'Amount', 'Category', 'Date'])
            for transaction in transactions:
                writer.writerow([transaction['id'], transaction['type'], transaction['amount'], transaction['category'],
                                 transaction['date']])

        # Send the CSV file to the user
        with open(csv_file_path, 'rb') as file:
            update.message.reply_document(document=file, filename=os.path.basename(csv_file_path))

        # Optionally, delete the CSV file after sending it
        os.remove(csv_file_path)

    except Exception as e:
        update.message.reply_text(f"An error occurred while exporting transactions: {e}")

