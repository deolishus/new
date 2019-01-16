from picamera import PiCamera
from time import sleep

input = int(input("1 to quit."> ))

camera = PiCamera()

camera.start_preview()


if input = 1:
    camera.stop_preview()
else:
    print("smile!")
