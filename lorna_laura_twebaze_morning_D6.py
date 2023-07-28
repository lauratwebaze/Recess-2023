# Receipt book Gui app
import tkinter as tk


def save_receipt():
    # Get the input values from the entry fields
    name = name_entry.get()
    amount = amount_entry.get()

    # Save the receipt to a file
    with open("receipts.txt", "a") as file:
        file.write(f"Name: {name}\nAmount: {amount}\n\n")

    # Clear the input fields
    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


def clear_receipts():
    # Clear the receipts file
    open("receipts.txt", "w").close()
    print("Receipts cleared.")


# Create the main window
window = tk.Tk()
window.title("Receipt Book App")

# Create and pack the input fields
name_label = tk.Label(window, text="Name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

amount_label = tk.Label(window, text="Amount:")
amount_label.pack()

amount_entry = tk.Entry(window)
amount_entry.pack()

# Create and pack the buttons
save_button = tk.Button(window, text="Save Receipt", command=save_receipt)
save_button.pack()

clear_button = tk.Button(window, text="Clear Receipts", command=clear_receipts)
clear_button.pack()

# Run the application
window.mainloop()
