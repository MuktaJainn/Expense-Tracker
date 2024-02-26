import tkinter as tk
from tkinter import messagebox

class ExpenseTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")
        self.master.geometry("600x600")  # Increased size for a better display

        # Frame with a background color
        self.frame = tk.Frame(master, bg="#f0f0f0")  # Light gray background color
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.expenses = {}

        # Entry widgets with a more visually appealing appearance
        entry_style = {"font": ("Arial", 12), "bg": "#e6e6e6", "bd": 2, "relief": tk.GROOVE}

        self.amount_label = tk.Label(self.frame, text="Amount (Rs):", **entry_style)
        self.amount_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.amount_entry = tk.Entry(self.frame, **entry_style)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.description_label = tk.Label(self.frame, text="Description:", **entry_style)
        self.description_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.description_entry = tk.Entry(self.frame, **entry_style)
        self.description_entry.grid(row=1, column=1, padx=10, pady=10)

        # Button to add expense with color and increased width
        self.add_button = tk.Button(self.frame, text="Add Expense", command=self.add_expense, bg="#4CAF50", fg="white", width=20, font=("Arial", 12))
        self.add_button.grid(row=2, column=0, columnspan=2, pady=30)

        # Display total expenses with color
        self.total_label = tk.Label(self.frame, text="Total Expenses: Rs. 0.00", font=("Arial", 14, "bold"), fg="#3333cc", bg="#f0f0f0")
        self.total_label.grid(row=3, column=0, columnspan=2, pady=30)

        # Display detailed expenses with a more visually appealing appearance
        details_style = {"height": 8, "width": 40, "font": ("Arial", 12), "bg": "#e6e6e6", "bd": 2, "relief": tk.GROOVE}
        self.expense_details_label = tk.Label(self.frame, text="Expense Details:", font=("Arial", 14), bg="#f0f0f0")
        self.expense_details_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

        self.expense_details_text = tk.Text(self.frame, **details_style)
        self.expense_details_text.grid(row=4, column=1, padx=10, pady=10)

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            description = self.description_entry.get()

            if amount <= 0:
                messagebox.showwarning("Invalid Amount", "Please enter a valid positive amount.")
            else:
                if description not in self.expenses:
                    self.expenses[description] = 0

                self.expenses[description] += amount
                self.update_total_label()
                self.update_expense_details()
                self.clear_entries()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numerical amount.")

    def update_total_label(self):
        total = sum(self.expenses.values())
        self.total_label.config(text=f"Total Expenses: Rs. {total:.2f}")

    def update_expense_details(self):
        self.expense_details_text.delete(1.0, tk.END)
        for description, amount in self.expenses.items():
            self.expense_details_text.insert(tk.END, f"{description} : Rs. {amount:.2f}\n")

    def clear_entries(self):
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()