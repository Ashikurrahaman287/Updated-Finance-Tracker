import sqlite3

def connect_db():
    return sqlite3.connect('finance_bot.db')

def create_tables():
    with connect_db() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS transactions
                        (id INTEGER PRIMARY KEY, type TEXT, amount REAL, category TEXT, date TEXT)''')
        conn.execute('''CREATE TABLE IF NOT EXISTS budgets
                        (category TEXT PRIMARY KEY, amount REAL)''')

def add_transaction_to_db(type, amount, category):
    with connect_db() as conn:
        conn.execute('INSERT INTO transactions (type, amount, category, date) VALUES (?, ?, ?, date("now"))',
                     (type, amount, category))

def fetch_transactions(limit=None):
    with connect_db() as conn:
        if limit:
            cursor = conn.execute('SELECT * FROM transactions ORDER BY date DESC LIMIT ?', (limit,))
        else:
            cursor = conn.execute('SELECT * FROM transactions ORDER BY date DESC')
        return cursor.fetchall()

def fetch_budget(category):
    with connect_db() as conn:
        cursor = conn.execute('SELECT amount FROM budgets WHERE category = ?', (category,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

def set_budget(category, amount):
    with connect_db() as conn:
        conn.execute('INSERT OR REPLACE INTO budgets (category, amount) VALUES (?, ?)', (category, amount))

def get_total_transactions_by_type(transaction_type):
    with connect_db() as conn:
        cursor = conn.execute('SELECT SUM(amount) FROM transactions WHERE type = ?', (transaction_type,))
        result = cursor.fetchone()
        return result[0] if result[0] else 0.0

def get_total_transactions_by_category(category):
    with connect_db() as conn:
        cursor = conn.execute('SELECT SUM(amount) FROM transactions WHERE category = ?', (category,))
        result = cursor.fetchone()
        return result[0] if result[0] else 0.0
