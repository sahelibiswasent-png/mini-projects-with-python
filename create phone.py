import tkinter as tk
from tkinter import messagebox

class PhoneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Phone App")
        self.root.geometry("300x500")
        self.root.configure(bg="#2c2c2c")

        self.number = ""

        # Display screen
        self.display = tk.Entry(root, font=("Arial", 24), justify="right",
                                bg="#1a1a1a", fg="white", bd=0, insertbackground="white")
        self.display.pack(fill="x", padx=20, pady=20, ipady=10)

        # Buttons layout
        buttons = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["*", "0", "#"],
        ]

        for row in buttons:
            frame = tk.Frame(root, bg="#2c2c2c")
            frame.pack(pady=5)
            for btn in row:
                tk.Button(frame, text=btn, font=("Arial", 18), width=5, height=2,
                          bg="#3a3a3a", fg="white", activebackground="#555",
                          command=lambda b=btn: self.press(b)).pack(side="left", padx=5)

        # Call and Clear buttons
        ctrl_frame = tk.Frame(root, bg="#2c2c2c")
        ctrl_frame.pack(pady=10)

        tk.Button(ctrl_frame, text="Call", font=("Arial", 14), width=7, height=2,
                  bg="#4CAF50", fg="white",
                  command=self.call).pack(side="left", padx=10)

        tk.Button(ctrl_frame, text="Clear", font=("Arial", 14), width=7, height=2,
                  bg="#f44336", fg="white",
                  command=self.clear).pack(side="left", padx=10)

    def press(self, key):
        self.number += key
        self.display.delete(0, tk.END)
        self.display.insert(0, self.number)

    def call(self):
        if self.number:
            messagebox.showinfo("Calling", f"Calling {self.number}...")
        else:
            messagebox.showwarning("Warning", "Please enter a number!")

    def clear(self):
        self.number = ""
        self.display.delete(0, tk.END)

root = tk.Tk()
app = PhoneApp(root)
root.mainloop()