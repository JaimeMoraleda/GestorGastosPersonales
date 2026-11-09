
# Personal Expense Tracker

A Python application to manage personal income and expenses, track savings and visualize spending habits.

## Features

- Register income and expenses.
- Organize transactions by categories.
- Store financial data using SQLite.
- View transaction history.
- Calculate total income, expenses and net savings.
- Visualize expenses using Matplotlib.

## Technologies

- Python 3
- SQLite
- Matplotlib

## Project Structure

```text
PersonalExpenseTracker/
├── database/
│   ├── db.py
│   └── __init__.py
├── services/
│   ├── expense_manager.py
│   └── __init__.py
├── visualization/
│   ├── charts.py
│   └── __init__.py
├── data/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository.
2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

Follow the terminal menu to manage your personal finances.

## Future Improvements

- Monthly financial reports.
- Custom category management.
- Transaction editing and deletion.
- Expense limits and budgets.
- Unit testing with pytest.
- Graphical user interface.

## Author

Jaime Moraleda
