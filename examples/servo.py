###
# Authors : 
# Uros PETREVSKI <uros@nodesign.net>
# Ronan Yvergniaux <ronan@yvergniaux.fr
#		7 May 2014
###

###
#
#   How to use servomotor.py
#
###
from IoTPy.pyuper.ioboard import IoBoard
from IoTPy.pyuper.adc import ADC
from IoTPy.pyuper.utils import IoTPy_APIError, die
from time import sleep
from IoTPy.things.servomotor import Servo


try:
    u = IoBoard()
except IoTPy_APIError, e: # seems can't establish connection with the board
    details = e.args[0]
    die(details)


adc_pin=u.get_pin(ADC, 27)
myservo = Servo(u,22)

while True:
    val = adc_pin.read()
    degr = (val-0)*(180-0)/(1024-0)+0
    myservo.write(degr)
    degr = myservo.read()
    print "servo degree=", degr
    sleep(0.1)
    ###
    #sleep(1)
    #myservo.writeMilliseconds(1.5)
    #sleep(1)
    #val = myservo.readMilliseconds()
    #print "duty in ms =", val
    ###
