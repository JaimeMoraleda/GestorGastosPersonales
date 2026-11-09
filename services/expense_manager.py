
from datetime import date

from database.db import (
    add_transaction,
    get_transactions,
    get_summary,
    delete_transaction
)


def register_transaction(transaction_type, category, description, amount):

    if amount <= 0:
        print("El importe debe ser mayor que cero.")
        return

    if not category.strip():
        print("La categoría no puede estar vacía.")
        return

    current_date = date.today().isoformat()

    add_transaction(
        current_date,
        transaction_type,
        category,
        description,
        amount
    )

    print("Movimiento registrado correctamente.")


def show_transactions():

    transactions = get_transactions()

    if not transactions:
        print("Todavía no hay movimientos registrados.")
        return

    print("\n--- HISTORIAL DE MOVIMIENTOS ---")

    for transaction in transactions:

        transaction_id, transaction_date, transaction_type, category, description, amount = transaction

        print(
            f"ID: {transaction_id} | "
            f"Fecha: {transaction_date} | "
            f"Tipo: {transaction_type} | "
            f"Categoría: {category} | "
            f"Descripción: {description} | "
            f"Importe: {amount:.2f} €"
        )


def calculate_balance():

    summary = get_summary()

    income = 0
    expenses = 0

    for transaction_type, amount in summary:

        if transaction_type == "income":
            income = amount

        elif transaction_type == "expense":
            expenses = amount

    savings = income - expenses

    print("\n--- RESUMEN FINANCIERO ---")
    print(f"Ingresos: {income:.2f} €")
    print(f"Gastos: {expenses:.2f} €")
    print(f"Ahorro neto: {savings:.2f} €")

def remove_transaction():

    try:
        transaction_id = int(input("Introduce el ID del movimiento que quieres eliminar: "))

    except ValueError:
        print("Debes introducir un ID numérico.")
        return

    transactions = get_transactions()

    transaction_exists = any(
        transaction[0] == transaction_id
        for transaction in transactions
    )

    if not transaction_exists:
        print("No existe ningún movimiento con ese ID.")
        return

    confirmation = input(
        "¿Estás seguro de que quieres eliminarlo? (s/n): "
    ).lower().strip()

    if confirmation == "s":

        deleted = delete_transaction(transaction_id)

        if deleted:
            print("Movimiento eliminado correctamente.")
        else:
            print("No se ha podido eliminar el movimiento.")

    else:
        print("Eliminación cancelada.")
