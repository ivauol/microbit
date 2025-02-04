# Imports go at the top
from bme688 import *
from OLED import *
from microbit import *
import time

# bme688 and OLED are files that contain the code needed
# for some reason the microbit library does not work here

display.scroll('On')
print('Hello')

init_sensor() # to take temperature, humidity and pressure readings
init_gas_sensor() # to take gas sensor readings (eCO2, IAQScore, IAQPercentage) IAQ = Index for Air Quality
init_display() # initialise screen before using it


f = open('data.csv', 'w') # file we're going to write the data to

f.write('Time,Temperature,Humidity,Pressure,IQAScore,eCO2Value\n')
loop = True
display.show(Image.HAPPY) # shows happy face

numOfReadings = 0

while loop:
    read_data_registers()
    temp = calc_temperature()
    humidity = calc_humidity()
    pressure = calc_pressure()
    iaqScore, iaqPercent, eCO2Value = calc_air_quality()

    f.write("{},{},{},{},{},{}\n".format(str(numOfReadings * 5), str(temp), str(humidity), str(pressure), str(iaqScore), str(eCO2Value)))
    timeBefore = time.ticks_ms()

    numOfReadings += 1 
    print(numOfReadings)

    # increment and show num readings each time
    
    show("Temperature: {} C".format(temp), 0)
    show("Humidity: {} %".format(humidity), 1)
    show("Pressure: {} Pa".format(pressure), 2)
    show("IAQ Score: {}".format(iaqScore), 3)
    show("IAQ Percent: {} %".format(iaqPercent) , 4)
    show("eCO2 Value: {}".format(eCO2Value) + " ppm", 5)

    # showing the readings we've taken on the OLED screen on the Kitronik

    while time.ticks_diff(time.ticks_ms(), timeBefore) < 5000:

        if button_a.is_pressed() or (numOfReadings > 50):
            display.show(Image.DIAMOND)
            f.close()
            loop = False
            break

    sleep(500)
