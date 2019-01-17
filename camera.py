from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.annotate_text = "Hello world!"
camera.image_effect = 'cartoon'
camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
