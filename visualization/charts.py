
import tkinter as tk
from tkinter import messagebox

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from database.db import get_expenses_by_category, get_transactions


def show_charts_window(parent):

    expenses = get_expenses_by_category()
    transactions = get_transactions()

    if not transactions:
        messagebox.showinfo(
            "Sin datos",
            "Todavía no hay movimientos registrados.",
            parent=parent
        )
        return

    # Datos de gastos por categoría
    categories = [item[0] for item in expenses]
    amounts = [float(item[1]) for item in expenses]

    # Calcular ingresos y gastos totales
    total_income = 0
    total_expenses = 0

    for transaction in transactions:

        transaction_type = transaction[2]
        amount = float(transaction[5])

        if transaction_type == "income":
            total_income += amount
        elif transaction_type == "expense":
            total_expenses += amount

    # Crear ventana de gráficos
    window = tk.Toplevel(parent)
    window.title("Análisis financiero")
    window.geometry("1100x750")
    window.minsize(850, 600)
    window.configure(bg="#F3F5F9")

    tk.Label(
        window,
        text="Análisis financiero",
        font=("Segoe UI", 20, "bold"),
        fg="#172B4D",
        bg="#F3F5F9"
    ).pack(anchor="w", padx=25, pady=(20, 10))

    # Crear figura de Matplotlib
    figure = Figure(figsize=(11, 7), dpi=100)
    figure.subplots_adjust(
        left=0.08,
        right=0.96,
        top=0.91,
        bottom=0.10,
        hspace=0.35,
        wspace=0.30
    )

    grid = figure.add_gridspec(2, 2)

    # Gráfico 1: gastos por categoría
    ax1 = figure.add_subplot(grid[0, 0])

    if expenses:

        ax1.bar(categories, amounts)

        ax1.set_title("Gastos por categoría", fontweight="bold")
        ax1.set_xlabel("Categoría")
        ax1.set_ylabel("Importe (€)")
        ax1.tick_params(axis="x", rotation=25)

    else:
        ax1.text(
            0.5, 0.5,
            "Todavía no hay gastos registrados",
            ha="center",
            va="center"
        )
        ax1.set_title("Gastos por categoría", fontweight="bold")
        ax1.set_xticks([])
        ax1.set_yticks([])

    # Gráfico 2: distribución de gastos
    ax2 = figure.add_subplot(grid[0, 1])

    if expenses and sum(amounts) > 0:

        ax2.pie(
            amounts,
            labels=categories,
            autopct="%1.1f%%",
            startangle=90
        )

        ax2.set_title("Distribución de gastos", fontweight="bold")

    else:
        ax2.text(
            0.5, 0.5,
            "No hay gastos para representar",
            ha="center",
            va="center"
        )
        ax2.set_title("Distribución de gastos", fontweight="bold")
        ax2.set_xticks([])
        ax2.set_yticks([])

    # Gráfico 3: comparación entre ingresos y gastos
    ax3 = figure.add_subplot(grid[1, :])

    labels = ["Ingresos", "Gastos"]
    values = [total_income, total_expenses]

    ax3.bar(labels, values)

    ax3.set_title("Comparación entre ingresos y gastos", fontweight="bold")
    ax3.set_ylabel("Importe (€)")

    # Integrar Matplotlib dentro de Tkinter
    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True,
        padx=15,
        pady=(0, 15)
    )
