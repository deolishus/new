from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

input = int(input("1 to quit."> ))

if input = 1:
    camera.stop_preview()
else:
    print("smile!")
