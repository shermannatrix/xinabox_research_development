# cw02_led_pwm
# Created at 2019-06-30 16:31:14.480855

import pwm

duty = 0

pinMode(D26, OUTPUT)

while True:
    for i in range(-100, 100, 1):
        duty = 100 - abs(i)
        
        pwm.write(D26.PWM, 100, duty, MICROS)
        
        sleep(10)