from picamera import PiCamera
from time import sleep

camera = PiCamera()

try:
    camera.start_preview()
except KeyboardInterrupt:
    camera.stop_preview()
