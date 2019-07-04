# cw02_blink_led
# Created at 2019-06-30 16:16:25.145783

pinMode(D26, OUTPUT)

# loop forever
while True:
    digitalWrite(D26, HIGH)
    sleep(1000)
    digitalWrite(D26, LOW)
    sleep(1000)
