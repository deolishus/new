from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
pause(2000000)
camera.stop_preview()
