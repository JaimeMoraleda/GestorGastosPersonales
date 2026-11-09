from datetime import date, datetime

from database.db import (
    add_transaction,
    get_transactions,
    get_summary,
    delete_transaction,
    get_transactions_by_date
)
def register_transaction(
    transaction_type,
    category,
    description,
    amount,
    transaction_date=None
):
    if amount <= 0:
        raise ValueError("El importe debe ser mayor que cero.")

    if not category.strip():
        raise ValueError("La categoría no puede estar vacía.")

    if transaction_date is None:
        transaction_date = date.today().isoformat()

    add_transaction(
        transaction_date,
        transaction_type,
        category,
        description,
        amount
    )
