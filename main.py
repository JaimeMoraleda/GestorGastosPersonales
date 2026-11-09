
from database.db import initialize_database

from services.expense_manager import (
    register_transaction,
    show_transactions,
    calculate_balance,
    remove_transaction
)


from visualization.charts import show_expenses_chart


def show_menu():

    print("\n==============================")
    print("     PERSONAL EXPENSE TRACKER")
    print("==============================")

    print("1. Registrar ingreso")
    print("2. Registrar gasto")
    print("3. Consultar movimientos")
    print("4. Consultar balance")
    print("5. Mostrar gráfico de gastos")
    print("6. Eliminar movimiento")
    print("0. Salir")


def get_amount():

    while True:

        try:
            amount = float(
                input("Introduce el importe: ").replace(",", ".")
            )

            if amount <= 0:
                print("El importe debe ser mayor que cero.")
                continue

            return amount

        except ValueError:
            print("Introduce un importe numérico válido.")


def main():

    initialize_database()

    while True:

        show_menu()

        option = input("\nSelecciona una opción: ")

        if option == "1":

            amount = get_amount()
            category = input("Categoría del ingreso: ")
            description = input("Descripción: ")

            register_transaction(
                "income",
                category,
                description,
                amount
            )

        elif option == "2":

            amount = get_amount()
            category = input("Categoría del gasto: ")
            description = input("Descripción: ")

            register_transaction(
                "expense",
                category,
                description,
                amount
            )

        elif option == "3":

            show_transactions()

        elif option == "4":

            calculate_balance()

        elif option == "5":

            show_expenses_chart()

        elif option == "6":

            show_transactions()
            remove_transaction()
            
        elif option == "0":

            print("Gracias por utilizar Personal Expense Tracker.")
            break

        else:

            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
