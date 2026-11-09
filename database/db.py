
import sqlite3
from pathlib import Path

# Ruta donde se guardará la base de datos
DATABASE_PATH = Path(__file__).resolve().parent.parent / "data" / "expenses.db"


def connect():
    """Establece la conexión con la base de datos."""
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    """Crea la base de datos y la tabla si todavía no existen."""

    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            type TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            amount REAL NOT NULL CHECK(amount > 0)
        )
    """)

    connection.commit()
    connection.close()


def add_transaction(date, transaction_type, category, description, amount):
    """Guarda un ingreso o gasto en la base de datos."""

    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO transactions
        (date, type, category, description, amount)
        VALUES (?, ?, ?, ?, ?)
    """, (date, transaction_type, category, description, amount))

    connection.commit()
    connection.close()


def get_transactions():
    """Devuelve todos los movimientos registrados."""

    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM transactions
        ORDER BY date DESC, id DESC
    """)

    transactions = cursor.fetchall()
    connection.close()

    return transactions


def get_summary():
    """Calcula el total de ingresos y gastos."""

    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT type, SUM(amount)
        FROM transactions
        GROUP BY type
    """)

    summary = cursor.fetchall()
    connection.close()

    return summary


def get_expenses_by_category():
    """Calcula cuánto se ha gastado en cada categoría."""

    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM transactions
        WHERE type = 'expense'
        GROUP BY category
        ORDER BY SUM(amount) DESC
    """)

    expenses = cursor.fetchall()
    connection.close()

    return expenses

def delete_transaction(transaction_id):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM transactions WHERE id = ?",
        (transaction_id,)
    )

    deleted_rows = cursor.rowcount

    connection.commit()
    connection.close()

    return deleted_rows

def get_transactions_by_date(start_date, end_date):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM transactions
        WHERE date BETWEEN ? AND ?
        ORDER BY date DESC, id DESC
    """, (start_date, end_date))

    transactions = cursor.fetchall()
    connection.close()

    return transactions
