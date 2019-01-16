from picamera import PiCamera
from datetime import datetime
from signal import pause

camera = PiCamera()

def capture():
    datetime = datetime.now().isoformat()
    camera.capture('/home/pi/%s.jpg' % datetime)

take = int(input("Type a number> "))

if take = 1:
    camera.start_preview
elif take = 2:
    camera.stop_preview
else:
    camera.capture


pause()
