import serial

port = serial.Serial('/dev/tty.usbmodem102', 115200)

print('Started')

while True:
    message = port.readline().decode().strip()
    print(message)

# this doesn't work i think if it's not local (?)
