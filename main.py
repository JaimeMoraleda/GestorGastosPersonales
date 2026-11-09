
import tkinter as tk

from database.db import initialize_database
from gui import ExpenseTrackerApp


def main():

    initialize_database()

    root = tk.Tk()

    app = ExpenseTrackerApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()
