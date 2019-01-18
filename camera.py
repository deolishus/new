from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(2000000)
camera.stop_preview()
