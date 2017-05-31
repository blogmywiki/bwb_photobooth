# bwb_photobooth
A very simple tweeting Raspberry Pi Photo Booth for a school disco or fair.

This is a project created by 3 Picademy attendees at the Museum of London on 30th May 2017 in a couple of hours. The idea was to make the simplest possible photo booth that can be taught and built by pupils. We know we were reinventing the wheel somewhat - other photo booths are available - but we wanted to make the simplest one we could with the PiCamera's built-in filters and no GUI. We decided to make the photos square to look more like a certain modern social media imaging service.

## You will need:
* A Raspberry Pi. We used a model 3 but I think any would work.
* The official PiCamera module.
* Two push buttons.
* A breadboard.
* Some male-female and male-male jumper wires.
* Internet access.
* A Twitter account with mobile phone authentication enabled.

## Setting up the software
If you have an updated version of Raspbian, you probably have all the Python libraries you need. The main ones we use are GPIO Zero and Twython, and you will need to configure the latter and your Twitter account.

We followed the excellent instructions on the Raspberry Pi education web site: [Getting Started With the Twitter API] https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/worksheet/

You need to end up with a file called auth.py in the same directory as the photobooth script; it will contain your 4 secret keys which you will have gathered from the process of creating a new app on the Twitter web site.

## Setting up the hardware
You need two fleeting push buttons: the one to take photos is connected to GPIO 17 and the one to cycle through the filters is connected to GPIO 10. Connect the other side of both switches to GND on the Pi.

## Using it
Run bwb_photobooth.py - you should see a preview of your photo on screen. We made it translucent so we could control things behind it - you can make it more opaque by increasing the value in this line closer to 255:
```camera.start_preview(alpha=130)```
The button you wired up to GPIO 10 will cycle through the different filters. When you find one you like, press the other button. It will save the photo over the previous one and tweet it with the message in the script and a timestamp.

## As a lesson
I want to write up a lesson plan for this - it could go like this:
* Write Python script to take a photo.
* Add a button to trigger taking photo.
* Add a button to cycle through filters.
* Add text and timestamp.
* Add Tweeting, if appropriate to age group and setting.

## Our own learning
We all learned a lot: for example we found that `button.wait_for_press()` will only poll the button once and not do anything else, where as `effect.when_pressed = change_filter` will keep polling the other button in the background and call the change_filter function any time it is pressed. Thanks to Ben Nuttall for his help with this!

## The Future
* Make it run continuously and improve user experience.
* Add a thermal printer to print the photo in black and white.
* Instead of tweeting, upload the photo by FTP to a secure URL - important when children's photos cannot be put on social media for safeguarding reasons.
* Print thermal till roll slip with URL and/or QR code so photo can be accessed later.
* Add LEDs for status feedback.
* Put it in a box.
* PiZero version mounted on a huge selfie-stick.
* Coin-operated for fund-raising.

## Credits

A collaborative project by Andrew Brixey, Andrew Wright and Giles Booth (hence bwb!). Huge thanks to Ben Nuttall, the creator of GPIO Zero for putting us on the right path when we got stuck with polling buttons.

![Our 1st successful tweeted photo](https://github.com/blogmywiki/bwb_photobooth/raw/master/sample_photo.jpg "The team!")
