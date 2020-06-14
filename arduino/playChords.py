import serial
import time
ser = serial.Serial('COM9', 9600, timeout=0)
import winsound

while 1:
 try:
    value = str(ser.readline())
    print(value)
    value = (value[2:][:-5])
    if value == "G":
        winsound.PlaySound("C:\\Users\\grace\\Documents\\Harvard\\Hackathons\\musitar-arduino\\GMajor.wav", winsound.SND_NOWAIT)
    if value == "D":
        winsound.PlaySound("C:\\Users\\grace\\Documents\\Harvard\\Hackathons\\musitar-arduino\\DMajor.wav", winsound.SND_NOWAIT)
    if value == "Em":
        winsound.PlaySound("C:\\Users\\grace\\Documents\\Harvard\\Hackathons\\musitar-arduino\\Eminor.wav", winsound.SND_NOWAIT)
    if value == "C":
        winsound.PlaySound("C:\\Users\\grace\\Documents\\Harvard\\Hackathons\\musitar-arduino\\CMajor.wav", winsound.SND_NOWAIT)

    time.sleep(.5)
 except ser.SerialTimeoutException:
    print('Data could not be read')
    time.sleep(1)