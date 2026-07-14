import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    description = input("Enter Description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("\nExpense Added Successfully!\n")


def view_expenses():
    print("\n========== EXPENSES ==========\n")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print("{:<12} {:<15} {:<10} {}".format(*row))
    print()


def total_expense():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Expense: ₹{total:.2f}\n")


def category_summary():
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    print("\nCategory Summary\n")

    for key, value in summary.items():
        print(f"{key:<15} ₹{value:.2f}")

    print()


def monthly_summary():
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            month = row["Date"][:7]
            amount = float(row["Amount"])

            if month in summary:
                summary[month] += amount
            else:
                summary[month] = amount

    print("\nMonthly Summary\n")

    for month, amount in summary.items():
        print(month, " : ₹", amount)

    print()


def menu():
    while True:

        print("====== SpendWise ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Monthly Summary")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            monthly_summary()

        elif choice == "6":
            print("Thank You!")
            break

        else:
            print("Invalid Choice\n")


create_file()
menu()