import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class QueueGarageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FIFO Parking Management")
        self.root.geometry("450x550")
        
        # FIFO Logic: First-In, First-Out
        self.garage = []
        self.MAX_CAPACITY = 10
        
        # UI Layout
        tk.Label(root, text="FIFO Parking System", font=("Arial", 16, "bold"), pady=10).pack()
        
        # Display Area
        self.list_frame = tk.LabelFrame(root, text="Queue Status (Top is next to Exit)")
        self.list_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        self.listbox = tk.Listbox(self.list_frame, font=("Courier", 10))
        self.listbox.pack(padx=10, pady=10, fill="both", expand=True)

        # Input Section
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)
        tk.Label(self.input_frame, text="Plate Number:").grid(row=0, column=0)
        self.plate_entry = ttk.Entry(self.input_frame)
        self.plate_entry.grid(row=0, column=1, padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = QueueGarageApp(root)
    root.mainloop()