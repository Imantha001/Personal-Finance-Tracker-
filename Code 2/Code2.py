# IIT Student ID: 20230606
# UOW Student ID: W2084786

import json
# Import the json module for reading and writing JSON data
# (json = Java Script Object Notation)


# Global dictionary to store transactions
# Initialize an empty dictionary to store transaction data

transactions = {}

# Variables
amount = 0
category = 0
date= 0



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
        transactions = {}
        # Function to load transactions from a JSON file, If file not found, initialize an empty list



# Function to save transactions
def save_transactions():
    # Open the transactions.json file in write mode
    with open("transactions.json", "w") as file:
        # Use the json.dump function to write the transactions list to the file
        json.dump(transactions, file)


        
# This function reads transactions from a file and adds them to the 'transactions'
def read_bulk_transactions_from_file(filename):
    try:
        # Open the file for reading
        with open(filename, "r") as file:
            # Iterate over each line in the file
            for line in file:
                # Split the line into category, amount, and date
                category, amount, date = line.strip().split(',')
                # Convert amount to float
                amount = float(amount)
                # Check if the category already exists in the transactions dictionary
                if category not in transactions:
                    # If not, create a new empty list for the category
                    transactions[category] = []
                    # Append the transaction to the list of transactions for the category
                transactions[category].append({"amount": amount, "date": date})



        # Print success message if no exceptions occurred
        print("Transactions read from file successfully.")

    # Handle FileNotFoundError
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while reading transactions from file: {e}")



# Feature implementations
def add_transaction():
    # Prompt user for transaction details
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))
    date = input("Enter the date (YYYY-MM-DD): ")


    # Check if the category already exists in the transactions dictionary
    if category not in transactions:
        # If not, create a new empty list for the category
        transactions[category] = []

        # Add the transaction to the list
    transactions[category].append({"amount": amount, "date": date})
    # Save the updated transactions to file
    save_transactions()


    
# Function to view  transaction
def view_transactions():
    # Iterate through transactions with index using enumerate
    for index, (category, transaction_list) in enumerate(transactions.items(), 1):
        # Print the category name
        print(f"Category: {category}")
        # Iterate over each transaction in the transaction list
        for idx, transaction in enumerate(transaction_list, 1):
            # Print transaction details
            print(f"{idx}. Amount: {transaction['amount']}, Date: {transaction['date']}")
        print()



# Function to update a transaction
def update_transaction():
    # Display existing transactions
    view_transactions()
    # Ask user for the category name to update
    category = input("Enter the category of the transaction to update: ")
    # Check if the category exists in transactions
    if category in transactions:
        # Ask index number of transaction to update
        index = int(input("Enter the index of the transaction to update: ")) - 1
        # Check if the index is within the valid range
        if 0 <= index < len(transactions[category]):
            # Ask user to enter new amountt and date
            amount = float(input("Enter the new amount: "))
            date = input("Enter the new date (YYYY-MM-DD): ")

            # Update the transaction with new amount and data
            transactions[category][index] = {"amount": amount, "date": date}
            # Save updated trannactions
            save_transactions()
            print("Transaction updated successfully.")
        else:
            print("Invalid transaction index.")
    else:
        print("Category not found.")



# Function to delete a transaction
def delete_transaction():
    # Display existing transactions
    view_transactions()

    # Ask user for the category name to update
    category = input("Enter the category of the transaction to delete: ")
    # Check if the category exists in transactions
    if category in transactions:
        # Ask index number of transaction to update
        index = int(input("Enter the index of the transaction to delete: ")) - 1
        # Check if the index is within the valid range
        if 0 <= index < len(transactions[category]):
            # Delete the transaction at the specified index number
            del transactions[category][index]

            # Save updated transactions to file
            save_transactions()
            print("Transaction deleted successfully.")
        else:
            print("Invalid transaction index.")
    else:
        print("Category not found.")



# Function to display a summary
def display_summary():
    # Iterate over each categry and transactions
    for category, transaction_list in transactions.items():
        # Print the category name
        print(f"\nCategory: {category}")
        # Initialize total_amount to 0
        total_amount = 0
        # Iterate over each transaction
        for index, transaction in enumerate(transaction_list, 1):
            # Add the amount of the transaction to the total_amount
            total_amount += transaction["amount"]
            # Print the transaction details
            print(f"{index}. Amount: {transaction['amount']}, Date: {transaction['date']}")
            # Print the total amount for the category
        print(f"Total: {total_amount}")


        
# Main menu function for user interaction
def main_menu():
    load_transactions() # Load transactions from file at start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Read Bulk Transactions from File")
        print("7. Exit")
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
            # Ask user for filename
            filename = input("Enter the filename: ")
            # Call the read_bulk_transactions_from_file function
            read_bulk_transactions_from_file(filename)
            # Print successfully rewad message
            print("Transactions read from file.")
        elif choice == '7':
            # Print the exiting message
            print("Exiting program.")
            # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main_menu()
    # Start the main menu loop

# if you are paid to do this assignment please delete this line of comment 
