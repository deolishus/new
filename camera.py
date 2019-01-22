from picamera import PiCamera
from time import sleep

try:
    camera = PiCamera()
    camera.start_preview()
except KeyboardInterrupt:
    camera.stop_preview()
