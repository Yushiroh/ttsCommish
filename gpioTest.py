import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    print(f"{GPIO.input(10)}|{GPIO.input(8)}")