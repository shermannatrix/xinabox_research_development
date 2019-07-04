# xb_esp32_lux_example
# Created at 2019-06-30 16:45:34.433587

import streams
from xinabox.sl01 import sl01

streams.serial()

# SL01 instance
SL01_T = sl01.TSL4531(I2C0)

# configure and start TSL4531
SL01_T.init()

pinMode(D25, OUTPUT)
pinMode(D26, OUTPUT)

while True:
    lux = SL01_T.getLUX()   # return ambient light level as lux
    print('Light level: ', lux, ' LUX')
    
    if lux >= 151:
        digitalWrite(D26, HIGH)
        digitalWrite(D25, LOW)
    else:
        digitalWrite(D26, LOW)
        digitalWrite(D25, HIGH)
    
    sleep(1000)
