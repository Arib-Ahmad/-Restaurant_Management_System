import tkinter as tk
from tkinter import messagebox, font


menu = {}
order = []

#Functions
def update_menu_list():
    menu_list.delete(0, tk.END)
    for item, price in menu.items():
        menu_list.insert(tk.END, f"{item} - ₹{price:.2f}")

def add_item():
    item = item_entry.get()
    price = price_entry.get()

    if not item or not price:
        messagebox.showwarning("Input Error", "Please enter item name and price")
        return

    try:
        price = float(price)
        menu[item] = price
        update_menu_list()
        item_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        status_label.config(text=f"Added {item} to menu")
    except ValueError:
        messagebox.showerror("Invalid Price", "Enter a valid number")

def remove_item():
    selected = menu_list.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select an item to remove")
        return

    item = menu_list.get(selected).split(" - ")[0]
    del menu[item]
    update_menu_list()
    status_label.config(text=f"Removed {item}")

def add_to_order():
    selected = menu_list.curselection()
    if not selected:
        return

    item = menu_list.get(selected).split(" - ")[0]
    order.append(item)
    order_list.insert(tk.END, item)
    status_label.config(text=f"Added {item} to order")

def calculate_bill():
    total = 0
    bill_text.delete(1.0, tk.END)

    for item in order:
        price = menu[item]
        bill_text.insert(tk.END, f"{item}: ₹{price:.2f}\n")
        total += price

    bill_text.insert(tk.END, f"\nTotal Bill: ₹{total:.2f}")

def clear_order():
    order.clear()
    order_list.delete(0, tk.END)
    bill_text.delete(1.0, tk.END)
    status_label.config(text="Order cleared")

# GUI
root = tk.Tk()
root.title("Restaurant Management System")
root.geometry("850x500")
root.configure(bg="#1e1e1e")

heading_font = font.Font(family="Segoe UI", size=18, weight="bold")
text_font = font.Font(family="Segoe UI", size=10)

header = tk.Label(
    root,
    text="🍽 Restaurant Management System",
    font=heading_font,
    bg="#1e1e1e",
    fg="white"
)
header.pack(pady=10)


main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(fill=tk.BOTH, expand=True, padx=10)


left_frame = tk.Frame(main_frame, bg="#2b2b2b", padx=10, pady=10)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tk.Label(left_frame, text="Menu", fg="white", bg="#2b2b2b", font=text_font).pack()

menu_list = tk.Listbox(left_frame, font=text_font, height=10)
menu_list.pack(fill=tk.BOTH, expand=True, pady=5)

tk.Button(left_frame, text="Add to Order", command=add_to_order).pack(pady=5)

# Add Item
item_entry = tk.Entry(left_frame)
item_entry.pack(pady=3)
item_entry.insert(0, "Item Name")

price_entry = tk.Entry(left_frame)
price_entry.pack(pady=3)
price_entry.insert(0, "Price")

tk.Button(left_frame, text="Add Item", command=add_item).pack(pady=3)
tk.Button(left_frame, text="Remove Item", command=remove_item).pack(pady=3)


right_frame = tk.Frame(main_frame, bg="#2b2b2b", padx=10, pady=10)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Label(right_frame, text="Order", fg="white", bg="#2b2b2b", font=text_font).pack()

order_list = tk.Listbox(right_frame, font=text_font, height=6)
order_list.pack(fill=tk.BOTH, expand=True, pady=5)

tk.Button(right_frame, text="Calculate Bill", command=calculate_bill).pack(pady=5)
tk.Button(right_frame, text="Clear Order", command=clear_order).pack(pady=3)

bill_text = tk.Text(right_frame, height=8, font=text_font)
bill_text.pack(fill=tk.BOTH, expand=True, pady=5)


status_label = tk.Label(
    root,
    text="Ready",
    bg="#111",
    fg="white",
    anchor="w",
    padx=10
)
status_label.pack(fill=tk.X, side=tk.BOTTOM)

root.mainloop()
