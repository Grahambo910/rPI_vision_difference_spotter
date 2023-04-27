import tkinter as tk
from tkinter import ttk
import os
import core

def update_nominal_label():
    num_nominal_photos = len(nominal_images)
    nominal_label_text.set(f"Nominal photos: {num_nominal_photos}\nDifferences: {nominal_differences}")

def update_discrepancy_label():
    num_discrepancy_photos = len(discrepancy_differences)
    discrepancy_label_text.set(f"Discrepancy photos: {num_discrepancy_photos}\nDifferences: {discrepancy_differences}")

def on_nominal_button_click():
    # Use the core.capture_photo and core.compare_images functions
    if not nominal_images:  # If there are no nominal images, initialize the first one
        image_name = 'nominal_1.jpg'
        trigger_power_button()
        time.sleep(delay)
        capture_photo(image_name)
        nominal_images.append(image_name)
    else:
        last_nominal_image = nominal_images[-1]
        image_name = f'nominal_{len(nominal_images) + 1}.jpg'
        trigger_power_button()
        time.sleep(delay)
        capture_photo(image_name)
        diff = compare_images(last_nominal_image, image_name)
        nominal_differences.append(diff)
        nominal_images.append(image_name)

    update_nominal_label()

def on_discrepancy_button_click():
    # Use the core.capture_photo and core.compare_images functions
    image_name = f'discrepancy_{len(discrepancy_differences) + 1}.jpg'
    trigger_power_button()
    time.sleep(delay)
    capture_photo(image_name)

    differences = [compare_images(nominal_image, image_name) for nominal_image in nominal_images]
    discrepancy_differences.append(differences)

    update_discrepancy_label()

def on_reset_button_click():
    for img in nominal_images:
        os.remove(img)
    for img in discrepancy_differences:
        os.remove(img)
    nominal_images.clear()
    nominal_differences.clear()
    discrepancy_differences.clear()

    update_nominal_label()
    update_discrepancy_label()

root = tk.Tk()
root.geometry("800x480")

nominal_images = []
nominal_differences = []
discrepancy_differences = []
delay = 30  # Adjust this value as needed (in seconds)

# Create the UI elements
# ... (same as before)

try:
    root.mainloop()
except KeyboardInterrupt:
    print("Interrupted. Cleaning up...")
finally:
    core.cleanup_gpio()
