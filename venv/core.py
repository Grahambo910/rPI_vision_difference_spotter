import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from PIL import Image
import imagehash
import cv2
import numpy as np

# Configure GPIO
GPIO.setmode(GPIO.BOARD)
RELAY_PINS = [11, 13, 15, 16, 18, 22, 29, 31]  # Change these to match the pins you're using
for pin in RELAY_PINS:
    GPIO.setup(pin, GPIO.OUT)

# Initialize the camera
camera = PiCamera()

def get_camera_frame():
    output = np.empty((96, 160, 3), dtype=np.uint8)
    camera.capture(output, 'rgb')
    return Image.fromarray(output)

def trigger_relay_module(relay_index):
    if relay_index < 0 or relay_index >= len(RELAY_PINS):
        raise ValueError("Invalid relay index")

    pin = RELAY_PINS[relay_index]
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.LOW)

def capture_photo(image_name):
    camera.capture(image_name)

def compare_images(image1, image2):
    hash1 = imagehash.average_hash(Image.open(image1))
    hash2 = imagehash.average_hash(Image.open(image2))
    return hash1 - hash2

def cleanup_gpio():
    GPIO.cleanup()
