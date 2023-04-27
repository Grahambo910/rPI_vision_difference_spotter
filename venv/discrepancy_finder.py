import time
import tkinter as tk
from tkinter import filedialog
import core

# Define your threshold and delay
THRESHOLD = 10  # Change this to your actual threshold
DELAY = 5  # Delay in seconds before taking a picture
RELAY_INDEX = 0  # Change this to the relay you want to use (0-7 for an 8x relay module)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.nominal_image = None

        self.start_button = tk.Button(self)
        self.start_button["text"] = "Start"
        self.start_button["command"] = self.start_test
        self.start_button.pack(side="top")

        self.stop_button = tk.Button(self)
        self.stop_button["text"] = "Stop"
        self.stop_button["command"] = self.stop_test
        self.stop_button.pack(side="top")

        self.reset_button = tk.Button(self)
        self.reset_button["text"] = "Reset"
        self.reset_button["command"] = self.reset_counter
        self.reset_button.pack(side="top")

        self.select_button = tk.Button(self)
        self.select_button["text"] = "Select Nominal Image"
        self.select_button["command"] = self.select_nominal_image
        self.select_button.pack(side="top")

        self.counter_label = tk.Label(self)
        self.counter_label.pack(side="top")

        self.discrepancy_label = tk.Label(self)
        self.discrepancy_label.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def select_nominal_image(self):
        self.nominal_image = filedialog.askopenfilename()

    def start_test(self):
        self.test_running = True
        self.counter = 0
        self.discrepancies = 0
        self.run_test()

    def stop_test(self):
        self.test_running = False

    def reset_counter(self):
        self.counter = 0
        self.discrepancies = 0
        self.update_labels()

    def update_labels(self):
        self.counter_label["text"] = f"Cycles: {self.counter}"
        self.discrepancy_label["text"] = f"Discrepancies: {self.discrepancies}"

    def run_test(self):
        if not self.test_running:
            return

        core.trigger_relay_module(RELAY_INDEX)
        time.sleep(DELAY)
        new_image = "new_image_{}.jpg".format(time.time())
        core.capture_photo(new_image)
        difference = core.compare_images(self.nominal_image, new_image)
        if difference > THRESHOLD:
            self.discrepancies += 1
        self.counter += 1
        self.update_labels()
        self.after(1000, self.run_test)  # run the test again in 1 second

root = tk.Tk()
app = Application(master=root)
app.mainloop()
