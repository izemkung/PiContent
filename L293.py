import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

class Motor:

    def __init__(self, pinForward, pinBackward, pinEn):
        """ Initialize the motor with its control pins and start pulse-width
             modulation """

        self.pin1 = pinForward
        self.pin2 = pinBackward
        self.pinEn = pinEn
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pinControl, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pinEn, 100)
        self.pwm.start(0)
        GPIO.output(self.pin1,GPIO.LOW)
        GPIO.output(self.pin2,GPIO.LOW)  

    def forward(self, speed):
        GPIO.output(self.pin1,GPIO.LOW)
        GPIO.output(self.pin2,GPIO.HIGH)      
        self.pwm.ChangeDutyCycle(speed)
         

    def backward(self, speed):
        GPIO.output(self.pin1,GPIO.HIGH)
        GPIO.output(self.pin2,GPIO.LOW)      
        self.pwm.ChangeDutyCycle(speed)

    def stop(self):
        GPIO.output(self.pin1,GPIO.LOW)
        GPIO.output(self.pin2,GPIO.LOW)      
        self.pwm.ChangeDutyCycle(0)

motor1 = Motor(18, 22, 16)
motor2 = Motor(21, 23, 19)

# Motor 1 test
motor1.forward(90)
sleep(5)
motor1.backward(50)
sleep(5)
motor1.stop()


# Motor 2 test
motor2.forward(90)
sleep(5)
motor2.backward(30)
sleep(5)
motor2.stop()

# Running both
motor1.forward(20)
motor2.backward(70)
sleep(5)
motor1.forward(90)
sleep(5)
motor1.stop()
motor2.stop()


GPIO.cleanup()