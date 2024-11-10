import tkinter as tk
from tkinter import ttk
# Import tkinter and ttk for GUI creation
import json
# Import json module for handling JSON data



# Create the FinanceTrackerGUI class for the application
class FinanceTrackerGUI:
    def __init__(self, root):
        # Initialize the root window
        self.root = root
        # Set the title of the root window
        self.root.title("Personal Finance Tracker")
        # Create the GUI widgets
        self.create_widgets()
        # Load transactions from the JSON file
        self.transactions = self.load_transactions("transactions.json")
        # Display the loaded transactions
        self.display_transactions(self.transactions)
        # Dictionary to track sorting order for each column
        self.sort_order = {}  


    # create GUI widget
    def create_widgets(self):
        # Frame for table and scrollbar
        self.table_frame = ttk.Frame(self.root)
        # Pack the frame to fill
        self.table_frame.pack(fill=tk.BOTH, expand=True) 


        # Treeview for displaying transactions
        self.transaction_tree = ttk.Treeview(self.table_frame, columns=("Amount", "Category", "Date"))
        # Set the heading for the first column (ID)
        self.transaction_tree.heading("#0", text="ID")
        # Set the heading and sorting  for the amount column
        self.transaction_tree.heading("Amount", text="Amount", command=lambda: self.sort_by_column("Amount"))
        # Set the heading and sorting  for the category column
        self.transaction_tree.heading("Category", text="Category", command=lambda: self.sort_by_column("Category"))
        # Set the heading and sorting  for the date column
        self.transaction_tree.heading("Date", text="Date", command=lambda: self.sort_by_column("Date"))
        # Pack the Treeview and filling both horizontally and vertically
        self.transaction_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)



        # Scrollbar for the Treeview
        self.tree_scroll = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.transaction_tree.yview)
        # Pack the scrollbar to the right side
        self.tree_scroll.pack(side=tk.RIGHT, fill="y")
        self.transaction_tree.configure(yscrollcommand=self.tree_scroll.set)



        # Search bar and button
        self.search_entry = ttk.Entry(self.root)
        # Pack the entry widget
        self.search_entry.pack()
        # Create a button for the search
        self.search_button = ttk.Button(self.root, text="Search", command=self.search_transactions)
        self.search_button.pack()


    # Try to open the specified JSON file for reading
    def load_transactions(self, filename):
        try:
            with open(filename, "r") as file:
                # Load the transactions from the JSON file
                transactions = json.load(file)
            # Return the loaded transactions
            return transactions
        # Error handing
        except FileNotFoundError:
            return {}



    def display_transactions(self, transactions):
        # Remove existing entries
        for item in self.transaction_tree.get_children():
            self.transaction_tree.delete(item)


        # Add transactions to the treeview
        for category, transaction_list in transactions.items():
            for idx, transaction in enumerate(transaction_list, 1):
                # Format the text as "category-index" and display transation details
                self.transaction_tree.insert("", "end", text=f"{category}-{idx}", values=(transaction["amount"], category, transaction["date"]))


    def search_transactions(self):
        # Get the search detail and convert it to lowercase
        search_term = self.search_entry.get().lower()
        # Check if the search is included
        if search_term:
            # Create a dictionary to store search results
            search_result = {}

            # Iterate through category and its transaction list
            for category, transaction_list in self.transactions.items():
                # Filter serch details and store it
                search_result[category] = [transaction for transaction in transaction_list if
                                           "amount" in transaction and search_term in str(transaction["amount"]).lower() or
                                           "category" in transaction and search_term in transaction["category"].lower() or
                                           "date" in transaction and search_term in transaction["date"].lower() or
                                           search_term in category.lower()]
            # Display the search results    
            self.display_transactions(search_result)
        else:
            # Display all deails
            self.display_transactions(self.transactions)


    def sort_by_column(self, col):
        # Toggle sorting order for the column
        if col in self.sort_order:
            # If sorting order exists for the column, toggle it
            self.sort_order[col] = not self.sort_order[col]
        else:
            # If sorting order doesn't exist for the column, set it to ascending order
            self.sort_order[col] = True
        # Get the items in the treeview
        items = self.transaction_tree.get_children("")
        # Sort the items
        sorted_items = sorted(items, key=lambda x: self.transaction_tree.set(x, col), reverse=self.sort_order[col])
        # Rearrange the sorted items in the treeview
        for i in sorted_items:
            self.transaction_tree.move(i, "", "end")

def main():
    # Create the main application window
    root = tk.Tk()
    # Initialize the FinanceTrackerGUI
    app = FinanceTrackerGUI(root)
    # Start the event loop to run the GUI application
    root.mainloop()

# Call the main function to start the application
if __name__ == "__main__":
    main()
