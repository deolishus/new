from picamera import picamera
from datetime import datetime
from signal import pause

camera = PiCamera()

def capture():
    datetime = datetime.now().isoformat()
    camera.capture('/home/pi/%s.jpg' % datetime)

while True:
    number = int(input("Press 0"))
    for number == 0:
        def capture()
