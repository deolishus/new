from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.start_preview()
sleep(100)
camera.stop_preview()
