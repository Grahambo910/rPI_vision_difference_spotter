import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from PIL import Image
import imagehash

# Configure GPIO
GPIO.setmode(GPIO.BOARD)
RELAY_PIN = 11
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Initialize the camera
camera = PiCamera()

def trigger_power_button():
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(RELAY_PIN, GPIO.LOW)

def capture_photo(image_name):
    camera.capture(image_name)

def compare_images(image1, image2):
    hash1 = imagehash.average_hash(Image.open(image1))
    hash2 = imagehash.average_hash(Image.open(image2))
    return hash1 - hash2

def cleanup_gpio():
    GPIO.cleanup()
