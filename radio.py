from microbit import *
import radio

radio.config(channel=65, group=1)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        radio.send("Hi :)")

    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)