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
        
    def update_display(self):
        self.listbox.delete(0, tk.END)
        for i, car in enumerate(self.garage):
            prefix = "[EXIT NEXT] ->" if i == 0 else f"[{i+1}]"
            self.listbox.insert(tk.END, f" {prefix} {car['plate']} (Arrived: {car['arrival']})")

    def handle_arrival(self):
        if len(self.garage) >= self.MAX_CAPACITY:
            messagebox.showwarning("Garage Full", "Maximum capacity of 10 reached!")
            return

        plate = self.plate_entry.get().upper().strip()
        if not plate:
            messagebox.showwarning("Input Error", "Please enter a plate number.")
            return

        arrival_time = datetime.now().strftime("%H:%M:%S")
        # Enqueue: Add to the end of the list
        self.garage.append({"plate": plate, "arrival": arrival_time})
        
        self.update_display()
        self.plate_entry.delete(0, tk.END)
        
    def handle_departure(self):
        if not self.garage:
            messagebox.showerror("Empty", "The garage is currently empty.")
            return

        confirm_plate = self.plate_entry.get().upper().strip()
        if not confirm_plate:
            messagebox.showinfo("Instruction", "Enter the plate of the car at the exit to confirm departure.")
            return

        # FIFO: The car at index 0 is the one at the front
        front_car = self.garage[0]

        if confirm_plate == front_car['plate']:
            # Dequeue: Remove from the front (index 0)
            removed = self.garage.pop(0)
            self.update_display()
            self.plate_entry.delete(0, tk.END)
            
            messagebox.showinfo("Departure Receipt", 
                f"--- PARKING RECEIPT ---\n"
                f"Plate: {removed['plate']}\n"
                f"Arrival: {removed['arrival']}\n"
                f"Departure: {datetime.now().strftime('%H:%M:%S')}\n"
                f"Status: Safely Departed")
        else:
            messagebox.showerror("Queue Blocked", 
                f"Error: Car {confirm_plate} cannot leave yet.\n"
                f"Car {front_car['plate']} is at the front and must leave first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QueueGarageApp(root)
    root.mainloop()