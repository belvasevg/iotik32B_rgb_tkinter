import serial
import time


class IOTik:

    def __init__(self,comNum,comSpeed):

        self.mirco = serial.Serial(comNum,comSpeed)
        time.sleep(2)

    
    def set_serial_state(self,state:bool):
        if state:
            self.mirco.open()
        if not(state):
            self.mirco.close()

    def set_rgb(self,data:str):
        data+=';'
        dataBytes = bytes([ord(b) for b in data])
        print(dataBytes)
        self.mirco.write(dataBytes)
