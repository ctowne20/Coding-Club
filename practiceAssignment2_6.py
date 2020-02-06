# In Class Practice
# 2/6/2020
# Carrieann Towne

import sys
import math

list = [22, -2, 3, 6]

def sum(list):
	for x in list:
		summation += x
	
	return summation
	
check = 'not in Range'
def checkRange(value):
	if value > 4 and value < 12:
		check = 'in Range'
	else:
		check = 'not in Range'
		
	print(value, 'is', check)
		
	#return check
	
checkRange(5)
checkRange(14)
checkRange(9)
checkRange(0)

def checkUpperLower(string):
	upper = 0
	lower = 0
	for x in string:
		if (x.isupper() == True):
			upper+= 1
		elif (x.islower() == True):
			lower+= 1
	
	print('Uppercase letters: ',upper)
	print('Lowercase letters: ',lower)

checkUpperLower('Hello World! It has Been MI Mild winter until Today')


def evenNumbers(evenList):
	newList = []
	for x in evenList:
		if (x%2)== 0:
			newList.append(x)
			
	return newList
	
evenList = [1,8,15,5,4,9,514]
print(evenNumbers(evenList))

def squareRoot(sqrootList):
	newList = []
	for x in sqrootList:
		newList.append(math.isqrt(x))
		
	return newList


sqrootList = [1,64,121,9]
print(squareRoot(sqrootList))