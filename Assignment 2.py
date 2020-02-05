# Carrieann Towne
# 1/30/2020
# Assignment 2

# LTU Honor Code: "I have neither given nor received unauthorized aid 
#	in completing this work, nor have I presented someone else's work as my own."

import sys
sys.path.append(r'C:\Python27\ArcGIS10.6\Toolbox')
import someConstants
from someConstants import NAME
from someConstants import PI
from someConstants import INCHTOCENTIMETER

print('Name: ', NAME)

def funcRadius():
	radii = [3,5,6]
	print(radii)
	
	for x in radii:
		areaCircle = PI*x*x
		if areaCircle > 40:
			print('The area of a circle with radius', x, 'is:', areaCircle)
		
funcRadius()

inch = 6

def convertItoC(inch):
	centimeters = inch*INCHTOCENTIMETER
	print(inch, 'inch(es) =',centimeters ,'centimeters')

convertItoC(inch)