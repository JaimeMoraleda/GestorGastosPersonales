from datetime import date, datetime

from database.db import (
    add_transaction,
    get_transactions,
    get_summary,
    delete_transaction,
    get_transactions_by_date
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

def filter_transactions_by_date():

    print("\n--- FILTRAR MOVIMIENTOS POR FECHAS ---")
    print("Formato de fecha: AAAA-MM-DD")
    
    try:
        start_date = input("Introduce la fecha inicial: ").strip()
        datetime.strptime(start_date, "%Y-%m-%d")

        end_date = input("Introduce la fecha final: ").strip()
        datetime.strptime(end_date, "%Y-%m-%d")

    except ValueError:
        print("Error: introduce fechas válidas con formato AAAA-MM-DD.")
        return

    if start_date > end_date:
        print("Error: la fecha inicial no puede ser posterior a la fecha final.")
        return

    transactions = get_transactions_by_date(start_date, end_date)

    if not transactions:
        print("No hay movimientos registrados en ese periodo.")
        return

    print("\n--- RESULTADOS DE LA BÚSQUEDA ---")

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

    print(f"\nTotal de movimientos encontrados: {len(transactions)}")
