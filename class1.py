from ev3dev.auto import *

Sound.speak('Welcome').wait()

motor = ev3.LargeMotor('outA')
hand = ev3.MediumMotor('outB')
motor.run_timed(time_sp=3000, duty_cycle_sp=75)
motor.run_forever()
motor.stop()

ir = InfraredSensor()
ir.value()
ts  = TouchSensor()
ts.value()



