# Default categories for transactions
DEFAULT_CATEGORIES = ["General", "Groceries", "Entertainment", "Utilities"]

# Default budget limits for categories
DEFAULT_BUDGETS = {
    "General": 1000,
    "Groceries": 300,
    "Entertainment": 200,
    "Utilities": 150
}

# Notification settings
DAILY_SUMMARY_TIME = "08:00"  # Time to send daily summaries
BUDGET_ALERT_THRESHOLD = 0.8  # Threshold for budget alerts (e.g., 80% of budget)
