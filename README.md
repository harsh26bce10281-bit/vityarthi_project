# Inventory Management System

A simple command-line Inventory Management System developed in Python for the CSE1021 Introduction to Problem Solving and Programming course.

## Project Overview

The program allows a user to manage products in an inventory through a terminal-based menu.

### Features

1. Add a product
2. Remove a product
3. Search for a product
4. Update product quantity
5. Display all products
6. Find low-stock products
7. Calculate total inventory value
8. Save and load inventory data

The project uses Python dictionaries and functions and stores data locally using the `pickle` module.

## Project Structure

```text
inventory-management-system/
├── main.py
├── inventory.py
├── storage.py
├── requirements.txt
├── .gitignore
├── README.md
├── data/
│   └── inventory.pkl
└── report/
    └── PROJECT_REPORT.md
```

## Requirements

- Python 3.8 or newer
- No third-party Python packages are required.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/inventory-management-system.git
cd inventory-management-system
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Optional virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

There are no external dependencies, but the following command is safe to run:

```bash
pip install -r requirements.txt
```

### 4. Run the project

Windows:

```bash
python main.py
```

Linux/macOS:

```bash
python3 main.py
```

## How the Program Works

When the program starts, it loads previously saved inventory data from:

```text
data/inventory.pkl
```

The user selects an operation from the menu. Changes are saved whenever inventory data is modified and again when the program exits.

## Data Representation

The inventory is stored as a dictionary. Each product contains its name, price, and quantity.

Example:

```python
{
    "mouse": {
        "name": "Mouse",
        "price": 800,
        "quantity": 10
    }
}
```

## Algorithms Used

- Searching using dictionary lookup
- Counting/filtering low-stock products
- Summation for total inventory value
- Traversal using `for` loops
- Conditional decision-making using `if` statements
- Modular problem solving using functions

## Complexity

Let `n` be the number of products.

- Add product: average O(1)
- Search product: average O(1)
- Remove product: average O(1)
- Update quantity: average O(1)
- Display inventory: O(n)
- Find low-stock products: O(n)
- Calculate total inventory value: O(n)

The inventory data requires O(n) space.

## Example

```text
==========================================
        INVENTORY MANAGEMENT SYSTEM
==========================================
1. Add Product
2. Remove Product
3. Search Product
4. Update Quantity
5. Display Inventory
6. Show Low-Stock Products
7. Calculate Total Inventory Value
8. Exit
==========================================
```

## Notes

This is intentionally a command-line project and does not require a graphical interface, database, web server, or external package.

## Academic Integrity

Understand the complete project before submitting it. Modify the implementation, documentation, examples, and report according to your own work and your instructor's requirements.
