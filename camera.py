from picamera import PiCamera
from time import sleep

cam = PiCamera()

cam.vflip = True

cam.start_preview(fullscreen = True)
sleep(10)
cam.stop_preview()
