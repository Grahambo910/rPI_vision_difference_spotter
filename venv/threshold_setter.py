import tkinter as tk
from tkinter import ttk
import os
import time
import core

def update_nominal_label():
    num_nominal_photos = len(nominal_images)
    nominal_label_text.set(f"Nominal photos: {num_nominal_photos}\nDifferences: {nominal_differences}")

def update_discrepancy_label():
    num_discrepancy_photos = len(discrepancy_differences)
    discrepancy_label_text.set(f"Discrepancy photos: {num_discrepancy_photos}\nDifferences: {discrepancy_differences}")

def on_nominal_button_click():
    image_name = "nominal_{}.jpg".format(time.time())
    core.capture_photo(image_name)
    nominal_images.append(image_name)
    if len(nominal_images) > 1:
        difference = core.compare_images(nominal_images[-2], nominal_images[-1])
        nominal_differences.append(difference)
    update_nominal_label()

def on_discrepancy_button_click():
    image_name = "discrepancy_{}.jpg".format(time.time())
    core.capture_photo(image_name)
    difference = min(core.compare_images(nominal_image, image_name) for nominal_image in nominal_images)
    discrepancy_differences.append(difference)
    update_discrepancy_label()

def on_reset_button_click():
    global nominal_images, nominal_differences, discrepancy_differences
    nominal_images = []
    nominal_differences = []
    discrepancy_differences = []
    update_nominal_label()
    update_discrepancy_label()

root = tk.Tk()
root.geometry("800x480")

nominal_images = []
nominal_differences = []
discrepancy_differences = []

nominal_label_text = tk.StringVar()
nominal_label = tk.Label(root, textvariable=nominal_label_text)
nominal_label.place(x=20, y=90)

discrepancy_label_text = tk.StringVar()
discrepancy_label = tk.Label(root, textvariable=discrepancy_label_text)
discrepancy_label.place(x=420, y=90)

nominal_button = tk.Button(root, text="Nominal", command=on_nominal_button_click, width=20, height=5)
nominal_button.place(x=20, y=20)

discrepancy_button = tk.Button(root, text="Discrepancy", command=on_discrepancy_button_click, width=20, height=5)
discrepancy_button.place(x=420, y=20)

reset_button = tk.Button(root, text="Reset", command=on_reset_button_click, width=10, height=2)
reset_button.place(x=700, y=400)

root.mainloop()
