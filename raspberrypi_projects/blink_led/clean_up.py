import RPi.GPIO as GPIO

GPIO.setwarnings(False)
ledPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)
GPIO.cleanup()
