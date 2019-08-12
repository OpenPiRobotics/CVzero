import time
from gpiozero import Button
import picamera
import CVzero

tracker = CVzero.Tracker()
button = gpiozero.Button(2)

with picamera.PiCamera() as camera:
    # Check for mode
    if button.is_pressed:
        tracker.mode = 'learn'
    else:
        tracker.mode = 'tracker'
    # Grab an image and give it to CVzero
    camera.capture(output, 'rgb')
    tracker.new_image(ouput)
    # Print some properties depending on mode 
    if tracker.mode == 'learn':
        print(tracker.typical_rgb)
    elif tracker.mode == 'tracker:
        print(tracker.location, tracker.size)
        