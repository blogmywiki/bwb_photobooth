from picamera import PiCamera
import picamera
from time import sleep
from gpiozero import Button
import datetime as dt
from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

filters = ['none', 'emboss','sketch','cartoon','colorswap','posterise','oilpaint','watercolor']
filternumber = 0

camera = PiCamera()
button = Button(17)   # this button takes a picture
effect = Button(10)   # this button cycles through filters

def change_filter():
    global filternumber
    filternumber += 1
    if filternumber > len(filters)-1:
        filternumber = 0        
    camera.image_effect = filters[filternumber]

camera.resolution = (600, 600)
camera.start_preview(alpha=130)

effect.when_pressed = change_filter
button.wait_for_press()
start = dt.datetime.now()
camera.annotate_text = str("Picademy Leavers' Disco\n" + dt.datetime.now().strftime('%Y-%m-%d %H:%M'))
camera.annotate_background = picamera.Color('red')
camera.capture("/home/pi/photobooth.jpg")
photo = open('/home/pi/photobooth.jpg', 'rb')
message = "A tweeted photo from #picademy photobooth" + dt.datetime.now().strftime('%Y-%m-%d %H:%M')

twitter.update_status_with_media(status=message, media=photo)

camera.stop_preview()
