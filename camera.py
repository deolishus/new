from picamera import PiCamera
from time import sleep

camera = Picamera()

camera.start_preview()
pause(2000000)
camera.stop_preview()
