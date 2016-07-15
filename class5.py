#!/usr/bin/python 

from ev3dev.auto import * 
from time import sleep 

running = True 

left = LargeMotor('outB') 
right = LargeMotor('outC') 

ir = InfraredSensor() 

def start(speed):
	left.run_direct(duty_cycle_sp=speed) 
	right.run_direct(duty_cycle_sp=speed)

def walk(speed):
	left.duty_cycle_sp = speed
	right.duty_cycle_sp = speed

def stop():
	left.duty_cycle_sp = 0 
	right.duty_cycle_sp = 0	

start(50) 
while running: 
	distance = ir.value()
	walk(50) 
	if distance < 20: 
		stop() 
	sleep(0.1)





