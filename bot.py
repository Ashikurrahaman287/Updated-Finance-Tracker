from telegram.ext import Updater, CommandHandler
from commands import add_transaction, export_csv, get_report, set_budget, show_summary
from notifications import daily_summary, budget_alert
from data.database import create_tables

# Initialize the bot with the token
def main():
    # Create the database tables if they don't exist
    create_tables()

    # Initialize the updater and dispatcher
    updater = Updater("TOKEN")
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("Debt", add_transaction.add_debit))
    dp.add_handler(CommandHandler("Crd", add_transaction.add_credit))
    dp.add_handler(CommandHandler("Today", show_summary.today_summary))
    dp.add_handler(CommandHandler("Last7", show_summary.last_7_days_summary))
    dp.add_handler(CommandHandler("Last30", show_summary.last_30_days_summary))
    dp.add_handler(CommandHandler("SetBudget", set_budget.set_budget))
    dp.add_handler(CommandHandler("MonthlyReport", get_report.monthly_report))
    dp.add_handler(CommandHandler("ExportCSV", export_csv.export_csv))

    # Set up daily summary notification (runs every day at 8 PM)
    jq = updater.job_queue
    jq.run_daily(daily_summary.send_daily_summary, time=datetime.time(hour=20, minute=0, second=0))

    # Set up budget alert notification (checks every hour)
    jq.run_repeating(budget_alert.check_budget_alerts, interval=3600, first=0)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
