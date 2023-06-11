import RPi.GPIO as GPIO
import time

# Set the pin numbering mode
GPIO.setmode(GPIO.BCM)

# GPIO18 set up as output
GPIO.setup(18, GPIO.OUT)

# Start a loop
try:
    while True:
        GPIO.output(18, GPIO.HIGH)  # Turn GPIO18 ON
        time.sleep(3)               # Wait for 3 seconds
        GPIO.output(18, GPIO.LOW)   # Turn GPIO18 OFF
        time.sleep(3)               # Wait for 3 seconds
except KeyboardInterrupt:            # Exit cleanly on Ctrl+C
    GPIO.cleanup()                  
