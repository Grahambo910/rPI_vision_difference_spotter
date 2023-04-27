import tkinter as tk
from tkinter import messagebox
import core

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.nominal_images = []
        self.discrepancy_images = []

    def create_widgets(self):
        self.nominal_button = tk.Button(self)
        self.nominal_button["text"] = "Nominal"
        self.nominal_button["command"] = self.capture_nominal
        self.nominal_button.place(x=100, y=200, width=200, height=100)

        self.discrepancy_button = tk.Button(self)
        self.discrepancy_button["text"] = "Discrepancy"
        self.discrepancy_button["command"] = self.capture_discrepancy
        self.discrepancy_button.place(x=500, y=200, width=200, height=100)

        self.reset_button = tk.Button(self)
        self.reset_button["text"] = "Reset"
        self.reset_button["command"] = self.reset
        self.reset_button.place(x=350, y=400, width=100, height=50)

        self.nominal_label = tk.Label(self)
        self.nominal_label.place(x=100, y=350)

        self.discrepancy_label = tk.Label(self)
        self.discrepancy_label.place(x=500, y=350)

    def update_labels(self):
        nominal_diff = core.get_difference(self.nominal_images) if self.nominal_images else 0
        discrepancy_diff = core.get_difference(self.discrepancy_images) if self.discrepancy_images else 0
        discrepancy_range = core.get_difference_range(self.nominal_images, self.discrepancy_images)

        self.nominal_label["text"] = f"Nominal images: {len(self.nominal_images)}, difference: {nominal_diff}"
        self.discrepancy_label["text"] = f"Discrepancy images: {len(self.discrepancy_images)}, difference: {discrepancy_diff}, range: {discrepancy_range}"

    def capture_nominal(self):
        self.nominal_images.append(core.capture_photo())
        self.update_labels()

    def capture_discrepancy(self):
        self.discrepancy_images.append(core.capture_photo())
        self.update_labels()

    def reset(self):
        self.nominal_images = []
        self.discrepancy_images = []
        self.update_labels()

root = tk.Tk()
root.geometry("800x480")
app = Application(master=root)
app.mainloop()
