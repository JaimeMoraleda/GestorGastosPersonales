
import matplotlib.pyplot as plt

from database.db import get_expenses_by_category


def show_expenses_chart():

    expenses = get_expenses_by_category()

    if not expenses:
        print("No hay gastos para representar.")
        return

    categories = [item[0] for item in expenses]
    amounts = [item[1] for item in expenses]

    plt.figure(figsize=(10, 6))

    plt.bar(categories, amounts)

    plt.title("Gastos por categoría")
    plt.xlabel("Categorías")
    plt.ylabel("Importe (€)")

    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.show()
