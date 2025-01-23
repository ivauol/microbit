# code from team
# Server Microbit Code


# Imports go at the top
from microbit import *
import radio

uart.init(baudrate=115200)

# vital data structures and variables
data_list = []
ready_to_record = False
recieved_data = None

# The server must be able to send a request to the sensors for data.
# This can be done with a signal only the sensors would interact with
def radioRequestData():
    display.scroll("REQ")
    radio.send("REQUEST")

def radioLoop(ready_to_record, recieved_data):
    radio.config(channel=37, group=1)
    radio.on()
    # Sensor data will be sent through radio as a string, thus every instance must be stored seperately
    while True:
        try:
            message = str(uart.read().decode())
            if message == "R":
                #display.scroll(":D")
                radioRequestData()
                ready_to_record = True

        except:
            pass

        if ready_to_record == True:
            while recieved_data is None:
                try:
                    recieved_data = radio.receive()
                    #display.scroll(recieved_data)
                except:
                    pass

        if button_a.is_pressed(): # only will record data once a is pressed
            radioRequestData()
            ready_to_record = True

        if ready_to_record == True and recieved_data is not None:
            uart.write(recieved_data + "\n")
            ready_to_record = False
            recieved_data = None

radioLoop(ready_to_record, recieved_data)
