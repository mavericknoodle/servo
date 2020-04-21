from adafruit_servokit import ServoKit
import time



while True:
    kit = ServoKit(channels=16)

    kit.servo[0].angle = 0
    print("0")

    time.sleep(3)

    kit.servo[0].angle = 90
    print("90")

    time.sleep(3)

