# Gestor de Gastos Personales

Aplicación desarrollada en Python para gestionar ingresos y gastos personales, controlar el ahorro y analizar los hábitos financieros mediante estadísticas y gráficos.

## Características principales

- **Registro de movimientos:** permite registrar ingresos y gastos indicando categoría, descripción e importe.
- **Historial de movimientos:** consulta todos los movimientos registrados.
- **Balance financiero:** calcula los ingresos totales, los gastos y el ahorro acumulado.
- **Eliminación de movimientos:** permite eliminar operaciones mediante su identificador.
- **Filtros por fechas:** consulta los movimientos dentro de un periodo determinado.
- **Informes mensuales:** muestra los ingresos, gastos, ahorro y distribución de gastos por categoría de un mes concreto.
- **Visualización gráfica:** representa los gastos por categoría mediante gráficos.

## Tecnologías utilizadas

- Python
- SQLite
- Matplotlib

## Estructura del proyecto

```text
GestorGastosPersonales/
│
├── database/
│   ├── __init__.py
│   └── db.py
│
├── services/
│   ├── __init__.py
│   └── expense_manager.py
│
├── visualization/
│   ├── __init__.py
│   └── charts.py
│
├── data/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/JaimeMoraleda/GestorGastosPersonales.git
```

### 2. Acceder a la carpeta del proyecto

```bash
cd GestorGastosPersonales
```

### 3. Crear un entorno virtual

```bash
python -m venv venv
```

### 4. Instalar las dependencias

En Windows, ejecuta:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```powershell
.\venv\Scripts\python.exe main.py
```

## Base de datos

La aplicación utiliza SQLite para almacenar los movimientos financieros en una base de datos local.

La base de datos se inicializa automáticamente al ejecutar la aplicación por primera vez.

Cada movimiento almacena:

- Identificador.
- Fecha.
- Tipo de movimiento (ingreso o gasto).
- Categoría.
- Descripción.
- Importe.

## Objetivo del proyecto

Este proyecto tiene como objetivo desarrollar una aplicación práctica utilizando Python, aplicando conceptos de programación, gestión de bases de datos, organización del código mediante módulos y visualización de datos.

Además, forma parte de mi aprendizaje y desarrollo de proyectos personales para mejorar mis habilidades de programación.