import tkinter as tk
import customtkinter as ctk

class Application(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.nominal_button = ctk.CTkButton(self, text="Nominal", width=200, height=100)
        self.nominal_button.place(x=100, y=200)

        self.discrepancy_button = ctk.CTkButton(self, text="Discrepancy", width=200, height=100)
        self.discrepancy_button.place(x=500, y=200)

        self.reset_button = ctk.CTkButton(self, text="Reset", width=100, height=50)
        self.reset_button.place(x=350, y=400)

        self.nominal_label = ctk.CTkLabel(self)
        self.nominal_label.place(x=100, y=350)

        self.discrepancy_label = ctk.CTkLabel(self)
        self.discrepancy_label.place(x=500, y=350)

        self.video_feed_label = ctk.CTkLabel(self)
        self.video_feed_label.place(x=300, y=50)

        self.video_feed_button = ctk.CTkButton(self, text="Start Video Feed", width=200, height=30)
        self.video_feed_button.place(x=300, y=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x480")
    app = Application(master=root)
    app.mainloop()

# Create a standalone instance of Application for testing
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x480")
    app = Application(master=root)
    app.mainloop()