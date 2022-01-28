from pynput import keyboard
import RPi.GPIO as GPIO

mode=GPIO.getmode()
GPIO.cleanup()

Forward=26
Backward=20
Left=16
Right=19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
GPIO.setup(Left, GPIO.OUT)
GPIO.setup(Right, GPIO.OUT)

def forward():
    GPIO.output(Backward, GPIO.LOW)
    GPIO.output(Forward, GPIO.HIGH)
    print("Moving Forward")

def reverse():
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Backward, GPIO.HIGH)
    print("Moving Backward")

def stop():
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Backward, GPIO.LOW)
    print("Stopping")

def left():
    GPIO.output(Right, GPIO.LOW)
    GPIO.output(Left, GPIO.HIGH)
    print("Turning Left")

def right():
    GPIO.output(Left, GPIO.LOW)
    GPIO.output(Right, GPIO.HIGH)
    print("Turning Right")

def straight():
    GPIO.output(Left, GPIO.LOW)
    GPIO.output(Right, GPIO.LOW)
    print("Turning Straight")


# while (1):
#     forward(5)
#     reverse(5)
#     left(5)
#     right(5)
#     GPIO.cleanup()
moving = "none"
steering = "none"

def on_press(key):
    global moving, steering
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    print('Key pressed' + k)
    if k == 'w' or k=='s':
        if k == 'w' and moving == "none":
            moving = "forward"
            forward()
        elif k == 's' and moving == "none":
            moving = "reverse"
            reverse()

    elif k =='a' or k=='d':
        if k=='a':
            left()
        elif k=='d':
            right()


def on_release(key):
    global moving, steering
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    print('Key released' + k)
    if k == 'w' or k=='s':
        moving = "none"
        stop()
    elif k == 'a' or k=='d':
        straight()

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys
