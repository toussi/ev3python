#!/usr/bin/python

from ev3dev.auto import *
from time import sleep 

legs = LargeMotor('outB')
ir = InfraredSensor() 
ir.mode = 'IR-PROX'
btn = Button()
screen = Screen()


running = True

def stop():
	Leds.set_color(Leds.LEFT, Leds.GREEN)
	Leds.set_color(Leds.RIGHT,Leds.GREEN)
	legs.stop()

def stopall():
	Sound.speak("See you later").wait() 
	
def start():
	screen.clear()
	screen.draw.rectangle( (10,10, 50, 50) , fill="black") 
	screen.update()
	Leds.set_color(Leds.LEFT, Leds.RED)
        Leds.set_color(Leds.RIGHT,Leds.RED)
	legs.run_direct(duty_cycle_sp=50)

def turn():
	stop()
	Sound.tone([(1000, 500, 500)] * 3).wait()
	Sound.speak("Turning around").wait()

# Main program 
while running:
	start() 
	if ir.value() > 50: 
		legs.duty_cycle_sp=100

	if ir.value() < 20:
		turn() 

	if btn.backspace: 
		stop()
		running = False

	sleep(0.1) 

# leaving the program 
stopall() 

