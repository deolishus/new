from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(999999999999)
camera.stop_preview()
