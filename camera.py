from picamera import PiCamera
from datetime import datetime
from signal import pause

camera = PiCamera()

def capture():
    datetime = datetime.now().isoformat()
    camera.capture('/home/pi/%s.jpg' % datetime)

take = int(input("Hit 1 to take picture!"))

if take == 1:
    capture()
else:
    pause()

pause()
