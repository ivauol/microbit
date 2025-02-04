from microbit import *
import radio

radio.config(channel=8, group=1)
radio.on()

display.scroll('on')

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        print('sending')
        radio.send("Hi :)")
        print('sent')

    incoming = radio.receive()
    if incoming:
        display.scroll(incoming, wait=False)