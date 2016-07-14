#!/usr/bin/python 

from ev3dev import ev3
from time import sleep 

words = ['oh my god', 'bang', 'that hurts', 'what?']
current = 0

ir = ev3.InfraredSensor()
btn = ev3.Button()

legs =  ev3.LargeMotor('outB')
turn = ev3.MediumMotor('outA') 

ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.AMBER)

while not btn.any():
	# main loop 
	while ir.value() > 20:
		legs.run_timed(time_sp='1000', duty_cycle_sp='50') 
	legs.stop() 
 
	turn.run_timed(time_sp='2000', duty_cycle_sp='60') 
	ev3.Sound.speak( words [ current ] ).wait() 
	current = current + 1
	if current > len(words) -1 : 
		current = 0
	
	
	

	




