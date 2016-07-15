#!/usr/bin/python 
from ev3dev.auto import * 
from time import sleep 

ir = InfraredSensor() 
screen = Screen() 
btn = Button()

running = True 

while running: 
	screen.clear()
	height = ir.value() 
	
	if btn.backspace:	
		running=False

	screen.draw.rectangle ( (0, screen.yres - ( screen.yres - 100)   , screen.xres, height ), fill="black") 
	screen.update() 
	sleep(0.1) 	

