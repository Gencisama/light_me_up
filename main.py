import serial
import pyfirmata

import time
#
#arduino = serial.Serial('COM7', baudrate = 9600, timeout=1)

board = pyfirmata.Arduino('COM7')

#dummy = 0




def light():
    board.digital[8].write(1)
    time.sleep(0.5)
    board.digital[8].write(0)




#while True:

#    arduinoData =arduino.readline().decode('ascii')
#    print(arduinoData)
    #time.sleep(0.25)

