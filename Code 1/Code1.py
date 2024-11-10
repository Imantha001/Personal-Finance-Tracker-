# IIT Student ID: 20230606
# UOW Student ID: W2084786


import json
# Import the json module for reading and writing JSON data
# (json = Java Script Object Notation)


# Global list to store transactions
# Initialize an empty list to store transaction data
transactions = []

# Variables
amount = 0
category = 0
transaction_type = 0
date = 0


# File handling functions
def load_transactions():
    # Access the global variable transactions
    global transactions
    
    try:
        # Try to open and read the transactions.json file
        with open("transactions.json", "r") as file:
            # Load the content of the file into the transactions list
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []
# Function to load transactions from a JSON file, If file not found, initialize an empty list



            
# Function to save transactions
def save_transactions():
    # Open the transactions.json file in write mode
    with open("transactions.json", "w") as file:
        # Use the json.dump function to write the transactions list to the file
        json.dump(transactions, file)


# Feature implementations
def add_transaction():
    # Prompt user for transaction details
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    transaction_type = input("Enter the type (Income/Expense): ")
    date = input("Enter the date (YYYY-MM-DD): ")

    transaction = [amount, category, transaction_type, date]
    transactions.append(transaction)  # Add the transaction to the list
    save_transactions()  # Save transactions to file
    print("Transaction added successfully.")


    
# Function to view  transaction
def view_transactions():
    # Iterate through transactions with index using enumerate
    for index, transaction in enumerate(transactions, start=1):
        # Display each transaction with its details
        print(f"{index}. Amount: {transaction[0]}, Category: {transaction[1]}, Type: {transaction[2]}, Date: {transaction[3]}")

# Function to update a transaction
def update_transaction():
    view_transactions()  # Display existing transactions
    index = int(input("Enter the index of the transaction to update: ")) - 1
    # Subtracting 1 to match the index


    if 0 <= index < len(transactions):
        # Prompt user for new transaction details
        amount = float(input("Enter the new amount: "))
        category = input("Enter the new category: ")
        transaction_type = input("Enter the new type (Income/Expense): ")
        date = input("Enter the new date (YYYY-MM-DD): ")

        transactions[index] = [amount, category, transaction_type, date]
        save_transactions()  # Save updated transactions
        print("Transaction updated successfully.")
    else:
        print("Invalid transaction index.")
        # Inform the user if the selected index is out of range
        
# Function to delete a transaction
def delete_transaction():
    view_transactions()  # Display existing transactions
    index = int(input("Enter the index of the transaction to delete: ")) - 1
    # Subtracting 1 to match the index

    if 0 <= index < len(transactions):
        del transactions[index]  # Remove transaction from the list
        save_transactions()  # Save updated transactions
        print("Transaction deleted successfully.")
    else:
        print("Invalid transaction index.")


# Function to display a summary of income, expenses, and profit
def display_summary():
    # Calculate total income by summing up all "Income"
    total_income = sum(transaction[0] for transaction in transactions if transaction[2] == "Income")

    # Calculate total expenses by summing up all "Expense"
    total_expense = sum(transaction[0] for transaction in transactions if transaction[2] == "Expense")

    # Calculate profit by subtracting total expenses from total income
    profit = total_income - total_expense

    # Print the income , expense and profit
    print(f"Income: {total_income}")
    print(f"Expense: {total_expense}")
    print(f"Profit: {profit}")



# Main menu function for user interaction
def main_menu():
    load_transactions()  # Load transactions from file at start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        # Check the user's choice and action
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.") # Notify the user of an invalid choice

if __name__ == "__main__":
    main_menu()
    # Start the main menu loop

# if you are paid to do this assignment please delete this line of comment 


