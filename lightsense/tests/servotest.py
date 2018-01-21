from gpiozero import AngularServo,LED
from time import sleep

led = LED(2)
servo = AngularServo(21,min_angle=-45,max_angle=45)

led.on()

servo.angle = -45
sleep(10)

for i in range(91):
    servo.angle += 1
    sleep(1)

led.off()
