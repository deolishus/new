
from picamera import PiCamera
from datetime import datetime
from signal import pause

camera = PiCamera()
movie = int(input("Type a number and press enter> "))

while True:
    if movie == 1:
        camera.preview()
    else:
        camera.stop_preview()
