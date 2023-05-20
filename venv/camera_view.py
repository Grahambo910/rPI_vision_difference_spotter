import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.nominal_button = tk.Button(self)
        self.nominal_button["text"] = "Nominal"
        self.nominal_button.place(x=100, y=200, width=200, height=100)

        self.discrepancy_button = tk.Button(self)
        self.discrepancy_button["text"] = "Discrepancy"
        self.discrepancy_button.place(x=500, y=200, width=200, height=100)

        self.reset_button = tk.Button(self)
        self.reset_button["text"] = "Reset"
        self.reset_button.place(x=350, y=400, width=100, height=50)

        self.nominal_label = tk.Label(self)
        self.nominal_label.place(x=100, y=350)

        self.discrepancy_label = tk.Label(self)
        self.discrepancy_label.place(x=500, y=350)

        self.video_feed_label = tk.Label(self)
        self.video_feed_label.place(x=300, y=50)

        self.video_feed_button = tk.Button(self)
        self.video_feed_button["text"] = "Start Video Feed"
        self.video_feed_button.place(x=300, y=20, width=200, height=30)

root = tk.Tk()
root.geometry("800x480")
app = Application(master=root)
app.mainloop()
