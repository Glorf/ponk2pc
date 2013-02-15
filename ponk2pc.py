#!/usr/bin/env python
import serial
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
while 1:
     rl=ser.readline().strip().decode("utf-8")
     while rl!="":
          print(rl)
          rl=ser.readline().strip().decode("utf-8")
     i=input()
     ser.write(i.encode("utf-8"))

ser.close()
