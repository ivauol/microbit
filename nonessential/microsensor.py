#code from team
#Microbit Sensor Code

from microbit import *
from OLED import *
from bme688 import *
import radio

def gatherDataFunc():
    init_sensor()
    init_gas_sensor()
    init_display()

    loop = True
    display.show(Image.HAPPY)
    numOfReadings = 0

    read_data_registers()
    current_temp = calc_temperature()
    current_humidity = calc_humidity()
    current_pressure = calc_pressure()
    current_iaqScore, current_iaqPercent, current_eCO2Value = calc_air_quality()
    timeBefore = time.ticks_ms()

    data_string = "{},{},{},{},{},{}".format(
    str(current_temp),
    str(current_humidity),
    str(current_pressure),
    str(current_iaqScore),
    str(current_iaqPercent),
    str(current_eCO2Value),
    )

    numOfReadings += 1
    #display.scroll(data_string)
    return data_string

def radioSendFunc():
    data = gatherDataFunc()
    radio.send(data)
    display.scroll("SENDING...")

def requestRecievedLoop():
    value = 0
    while value == 0:
       if button_a.was_pressed() or accelerometer.was_gesture("shake"):
            value = 1
            radioSendFunc()

def radioReceiveLoop():
    radio.config(channel=37, group=1)
    radio.on()
    display.show("W")

    while True:
        display.show("W")
        recieve = radio.receive()
        if recieve == "REQUEST":
            display.show("R")
            requestRecievedLoop()


radioReceiveLoop()
