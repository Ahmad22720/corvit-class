import os
import sys
import tkinter as tk
from tkinter import messagebox, ttk


# Allow running this file directly while importing project modules from parent folder
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, ".."))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from rental_service import RentalService  # noqa: E402
from car import Car  # noqa: E402
from bike import Bike  # noqa: E402
from customer import Customer  # noqa: E402


class RentalGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vehicle Rental System (GUI)")
        self.geometry("900x600")

        self.service = RentalService()
        self._seed_data()

        self._build_ui()

    def _seed_data(self):
        # Vehicles (same as your main.py idea; you can edit these)
        self.service.add_vehicle(Bike("B102", "sutlej", 2015, 1000, "125cc", "petrol"))
        self.service.add_vehicle(Car("C101", "Honda", 2016, 3000, "660cc", "petrol"))
        self.service.add_vehicle(Car("C102", "swift", 2020, 3000, "1200cc", "petrol"))
        self.service.add_vehicle(Car("C103", "tesla", 2026, 3000, "1000hp", "Electric"))

        # Customers
        self.service.register_customer(Customer("u1", "Ahmad"))
        self.service.register_customer(Customer("u2", "Ali"))

    def _build_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        header = ttk.Frame(self, padding=10)
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(0, weight=1)
        ttk.Label(
            header,
            text="Vehicle Rental System",
            font=("Segoe UI", 16, "bold"),
        ).grid(row=0, column=0, sticky="w")

        body = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        body.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

        left = ttk.Frame(body, padding=10)
        right = ttk.Frame(body, padding=10)
        body.add(left, weight=1)
        body.add(right, weight=2)

        # Left: actions + inputs
        ttk.Label(left, text="Actions", font=("Segoe UI", 11, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 8)
        )

        inputs = ttk.LabelFrame(left, text="Inputs", padding=10)
        inputs.grid(row=1, column=0, sticky="ew")
        inputs.columnconfigure(1, weight=1)

        self.customer_id_var = tk.StringVar()
        self.customer_name_var = tk.StringVar()
        self.vehicle_id_var = tk.StringVar()
        self.days_var = tk.StringVar()

        ttk.Label(inputs, text="Customer ID").grid(row=0, column=0, sticky="w")
        ttk.Entry(inputs, textvariable=self.customer_id_var).grid(
            row=0, column=1, sticky="ew", pady=2
        )

        ttk.Label(inputs, text="Customer Name").grid(row=1, column=0, sticky="w")
        ttk.Entry(inputs, textvariable=self.customer_name_var).grid(
            row=1, column=1, sticky="ew", pady=2
        )

        ttk.Label(inputs, text="Vehicle ID").grid(row=2, column=0, sticky="w")
        ttk.Entry(inputs, textvariable=self.vehicle_id_var).grid(
            row=2, column=1, sticky="ew", pady=2
        )

        ttk.Label(inputs, text="Days").grid(row=3, column=0, sticky="w")
        ttk.Entry(inputs, textvariable=self.days_var).grid(
            row=3, column=1, sticky="ew", pady=2
        )

        btns = ttk.Frame(left)
        btns.grid(row=2, column=0, sticky="ew", pady=10)
        btns.columnconfigure(0, weight=1)
        btns.columnconfigure(1, weight=1)

        ttk.Button(btns, text="Show Available", command=self.show_available).grid(
            row=0, column=0, sticky="ew", padx=(0, 6), pady=3
        )
        ttk.Button(btns, text="Show All", command=self.show_all).grid(
            row=0, column=1, sticky="ew", padx=(6, 0), pady=3
        )

        ttk.Button(btns, text="Search Vehicle", command=self.search_vehicle).grid(
            row=1, column=0, sticky="ew", padx=(0, 6), pady=3
        )
        ttk.Button(btns, text="View Customers", command=self.view_customers).grid(
            row=1, column=1, sticky="ew", padx=(6, 0), pady=3
        )

        ttk.Button(btns, text="Rent Vehicle", command=self.rent_vehicle).grid(
            row=2, column=0, sticky="ew", padx=(0, 6), pady=3
        )
        ttk.Button(btns, text="Return Vehicle", command=self.return_vehicle).grid(
            row=2, column=1, sticky="ew", padx=(6, 0), pady=3
        )

        ttk.Button(btns, text="Add Customer", command=self.add_customer).grid(
            row=3, column=0, sticky="ew", padx=(0, 6), pady=3
        )
        ttk.Button(btns, text="Clear Inputs", command=self.clear_inputs).grid(
            row=3, column=1, sticky="ew", padx=(6, 0), pady=3
        )

        # Right: output
        ttk.Label(right, text="Output", font=("Segoe UI", 11, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 8)
        )
        right.rowconfigure(1, weight=1)
        right.columnconfigure(0, weight=1)

        self.output = tk.Text(right, wrap="word", state="disabled")
        self.output.grid(row=1, column=0, sticky="nsew")

        scroll = ttk.Scrollbar(right, orient="vertical", command=self.output.yview)
        scroll.grid(row=1, column=1, sticky="ns")
        self.output.configure(yscrollcommand=scroll.set)

        self._write("Ready.\n")

    def _write(self, text: str):
        self.output.configure(state="normal")
        self.output.insert("end", text)
        self.output.see("end")
        self.output.configure(state="disabled")

    def clear_inputs(self):
        self.customer_id_var.set("")
        self.customer_name_var.set("")
        self.vehicle_id_var.set("")
        self.days_var.set("")

    def _get_customer(self, customer_id: str):
        for c in self.service.customers:
            if c.customer_id == customer_id:
                return c
        return None

    def _get_vehicle(self, vehicle_id: str):
        for v in self.service.vehicles:
            if v.vehicle_id == vehicle_id:
                return v
        return None

    def show_available(self):
        available = [v for v in self.service.vehicles if v.is_available]
        self._write("\nAvailable Vehicles\n")
        if not available:
            self._write("No vehicle is available.\n")
            return
        for v in available:
            self._write(self._format_vehicle(v) + "\n")

    def show_all(self):
        self._write("\nAll Vehicles\n")
        if not self.service.vehicles:
            self._write("No vehicles in system.\n")
            return
        for v in self.service.vehicles:
            status = "Available" if v.is_available else "Rented"
            self._write(self._format_vehicle(v) + f"Status : {status}\n\n")

    def search_vehicle(self):
        vehicle_id = self.vehicle_id_var.get().strip()
        if not vehicle_id:
            messagebox.showwarning("Missing", "Enter Vehicle ID.")
            return
        v = self._get_vehicle(vehicle_id)
        self._write(f"\nSearch Vehicle: {vehicle_id}\n")
        if not v:
            self._write("Vehicle not found.\n")
            return
        status = "Available" if v.is_available else "Rented"
        self._write(self._format_vehicle(v) + f"Status : {status}\n")

    def view_customers(self):
        self._write("\nCustomers\n")
        if not self.service.customers:
            self._write("No customers in system.\n")
            return
        for c in self.service.customers:
            rented = c.rented_vehicle.vehicle_id if c.rented_vehicle else "None"
            self._write(f"ID: {c.customer_id} | Name: {c.name} | Rented: {rented}\n")

    def add_customer(self):
        customer_id = self.customer_id_var.get().strip()
        name = self.customer_name_var.get().strip()
        if not customer_id or not name:
            messagebox.showwarning("Missing", "Enter Customer ID and Customer Name.")
            return
        if self._get_customer(customer_id):
            messagebox.showerror("Duplicate", "Customer ID already exists.")
            return
        self.service.register_customer(Customer(customer_id, name))
        self._write(f"\nCustomer added: {customer_id} ({name})\n")

    def rent_vehicle(self):
        customer_id = self.customer_id_var.get().strip()
        vehicle_id = self.vehicle_id_var.get().strip()
        days_raw = self.days_var.get().strip()

        if not customer_id or not vehicle_id or not days_raw:
            messagebox.showwarning(
                "Missing", "Enter Customer ID, Vehicle ID, and Days."
            )
            return

        try:
            days = int(days_raw)
            if days <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Invalid", "Days must be a positive number.")
            return

        c = self._get_customer(customer_id)
        v = self._get_vehicle(vehicle_id)
        if not c:
            messagebox.showerror("Not found", "Customer not found.")
            return
        if not v:
            messagebox.showerror("Not found", "Vehicle not found.")
            return
        if not v.is_available:
            messagebox.showerror("Unavailable", "Vehicle is not available.")
            return

        v.rent()
        c.rent_vehicle(v)
        cost = v.calculate_rental_cost(days)
        self._write(
            f"\nRented: {vehicle_id} to {customer_id} for {days} day(s). Cost: {cost} Pkr\n"
        )

    def return_vehicle(self):
        customer_id = self.customer_id_var.get().strip()
        if not customer_id:
            messagebox.showwarning("Missing", "Enter Customer ID.")
            return

        c = self._get_customer(customer_id)
        if not c:
            messagebox.showerror("Not found", "Customer not found.")
            return
        if not c.rented_vehicle:
            messagebox.showinfo("Nothing to return", "This customer has not rented any vehicle.")
            return

        v = c.rented_vehicle
        v.return_vehicle()
        c.return_vehicle()
        self._write(f"\nReturned: {v.vehicle_id} by {customer_id}\n")

    def _format_vehicle(self, v):
        lines = [
            f"ID : {v.vehicle_id}",
            f"Brand Name: {v.brand}",
            f"Model : {v.model}",
            f"Rental price per day : {v.rental_price_per_day}",
        ]
        # Show extra fields for subclasses if present
        if hasattr(v, "doors"):
            lines.append(f"Doors : {getattr(v, 'doors')}")
        if hasattr(v, "engine"):
            lines.append(f"Engine : {getattr(v, 'engine')}")
        if hasattr(v, "fuel_type"):
            lines.append(f"Fuel Type : {getattr(v, 'fuel_type')}")
        if hasattr(v, "type"):
            lines.append(f"Type : {getattr(v, 'type')}")
        return "\n".join(lines) + "\n"


if __name__ == "__main__":
    app = RentalGUI()
    app.mainloop()

