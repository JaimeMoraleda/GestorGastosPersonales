
import tkinter as tk
from tkinter import ttk, messagebox

from database.db import get_transactions


class ExpenseTrackerApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Gestor de Gastos Personales")
        self.root.geometry("1100x700")
        self.root.minsize(850, 550)
        self.root.configure(bg="#F3F5F9")

        self.setup_styles()
        self.create_widgets()
        self.refresh_data()

    def setup_styles(self):

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="white",
            foreground="#263238",
            rowheight=35,
            fieldbackground="white",
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview.Heading",
            background="#E8EDF5",
            foreground="#263238",
            font=("Segoe UI", 10, "bold"),
            padding=10
        )

        style.map(
            "Treeview",
            background=[("selected", "#D6E4FF")],
            foreground=[("selected", "#172B4D")]
        )

    def create_widgets(self):

        # Encabezado
        header = tk.Frame(self.root, bg="#172B4D", height=110)
        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="Gestor de Gastos Personales",
            font=("Segoe UI", 22, "bold"),
            fg="white",
            bg="#172B4D"
        )
        title.pack(anchor="w", padx=30, pady=(20, 0))

        subtitle = tk.Label(
            header,
            text="Controla tus ingresos, gastos y ahorro",
            font=("Segoe UI", 11),
            fg="#C5D3E8",
            bg="#172B4D"
        )
        subtitle.pack(anchor="w", padx=32)

        # Contenedor principal
        main_frame = tk.Frame(self.root, bg="#F3F5F9")
        main_frame.pack(fill="both", expand=True, padx=30, pady=25)

        # Título del resumen
        tk.Label(
            main_frame,
            text="Resumen financiero",
            font=("Segoe UI", 17, "bold"),
            fg="#172B4D",
            bg="#F3F5F9"
        ).pack(anchor="w", pady=(0, 15))

        # Tarjetas de resumen
        cards_frame = tk.Frame(main_frame, bg="#F3F5F9")
        cards_frame.pack(fill="x", pady=(0, 25))

        self.income_label = self.create_card(
            cards_frame, "INGRESOS", "#16865B"
        )

        self.expense_label = self.create_card(
            cards_frame, "GASTOS", "#D94B4B"
        )

        self.balance_label = self.create_card(
            cards_frame, "AHORRO", "#315DA8"
        )

        # Historial
        tk.Label(
            main_frame,
            text="Últimos movimientos",
            font=("Segoe UI", 17, "bold"),
            fg="#172B4D",
            bg="#F3F5F9"
        ).pack(anchor="w", pady=(0, 15))

        table_frame = tk.Frame(main_frame, bg="white")
        table_frame.pack(fill="both", expand=True)

        columns = (
            "id",
            "date",
            "type",
            "category",
            "description",
            "amount"
        )

        self.transaction_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.transaction_table.heading("id", text="ID")
        self.transaction_table.heading("date", text="Fecha")
        self.transaction_table.heading("type", text="Tipo")
        self.transaction_table.heading("category", text="Categoría")
        self.transaction_table.heading("description", text="Descripción")
        self.transaction_table.heading("amount", text="Importe")

        self.transaction_table.column("id", width=50, anchor="center")
        self.transaction_table.column("date", width=110, anchor="center")
        self.transaction_table.column("type", width=100, anchor="center")
        self.transaction_table.column("category", width=140)
        self.transaction_table.column("description", width=250)
        self.transaction_table.column("amount", width=110, anchor="e")

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.transaction_table.yview
        )

        self.transaction_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.transaction_table.pack(
            side="left", fill="both", expand=True, padx=(10, 0), pady=10
        )

        scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=10)

        # Botones inferiores
        buttons_frame = tk.Frame(main_frame, bg="#F3F5F9")
        buttons_frame.pack(fill="x", pady=(20, 0))

        refresh_button = tk.Button(
            buttons_frame,
            text="Actualizar datos",
            command=self.refresh_data,
            font=("Segoe UI", 10, "bold"),
            bg="#315DA8",
            fg="white",
            activebackground="#24477F",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        refresh_button.pack(side="left")

        exit_button = tk.Button(
            buttons_frame,
            text="Salir",
            command=self.root.destroy,
            font=("Segoe UI", 10, "bold"),
            bg="#E3E8F0",
            fg="#263238",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        exit_button.pack(side="right")

    def create_card(self, parent, title, color):

        card = tk.Frame(
            parent,
            bg="white",
            highlightbackground="#E0E5ED",
            highlightthickness=1
        )

        card.pack(side="left", fill="both", expand=True, padx=5)

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 10, "bold"),
            fg="#68778D",
            bg="white"
        ).pack(anchor="w", padx=18, pady=(15, 5))

        value_label = tk.Label(
            card,
            text="0.00 €",
            font=("Segoe UI", 20, "bold"),
            fg=color,
            bg="white"
        )

        value_label.pack(anchor="w", padx=18, pady=(0, 15))

        return value_label

    def refresh_data(self):

        try:
            transactions = get_transactions()

            total_income = 0
            total_expenses = 0

            # Limpiamos la tabla antes de actualizarla.
            for item in self.transaction_table.get_children():
                self.transaction_table.delete(item)

            # Calculamos ingresos y gastos.
            for transaction in transactions:

                transaction_id = transaction[0]
                transaction_date = transaction[1]
                transaction_type = transaction[2]
                category = transaction[3]
                description = transaction[4] or ""
                amount = transaction[5]

                if transaction_type == "income":
                    total_income += amount
                    displayed_type = "Ingreso"

                else:
                    total_expenses += amount
                    displayed_type = "Gasto"

                self.transaction_table.insert(
                    "",
                    "end",
                    values=(
                        transaction_id,
                        transaction_date,
                        displayed_type,
                        category,
                        description,
                        f"{amount:.2f} €"
                    )
                )

            balance = total_income - total_expenses

            self.income_label.config(
                text=f"{total_income:.2f} €"
            )

            self.expense_label.config(
                text=f"{total_expenses:.2f} €"
            )

            self.balance_label.config(
                text=f"{balance:.2f} €"
            )

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"No se han podido cargar los datos:\n{error}"
            )
