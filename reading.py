import smbus
import math
import time
import sys
import hmc5883l

compass = hmc5883l.hmc5883l(gauss = 4.7, declination = (-2,5))

test1 = compass.heading()
test2 = compass.axes()

#print test1
print test2