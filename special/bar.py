#!/usr/bin/python 
from ev3dev.auto import * 
from time import sleep 

ir = InfraredSensor() 
screen = Screen() 




while True: 
	screen.clear()
	height = ir.value() 

	screen.draw.rectangle ( (0, screen.yres - ( screen.yres - 100)   , screen.xres, height ), fill="black") 
	screen.update() 
	sleep(0.1) 	

