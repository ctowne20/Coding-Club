# Python Coding Club
# Assignment 3: Fancier Output & File Management
# February 20, 2020
# Carrieann Towne

# Honor Code: "I have neither given nor received unauthorized aid in 
# completing this work, nor have I presented someone else's work as my own"

import math
from toolboxAssignment3 import *
from someConstants import *

f = open("G:\My Drive\Spring 2020!\Python\Assignment Files\Assignment3File.txt","w+")

fileName = "G:\My Drive\Spring 2020!\Python\Assignment Files\printme.txt"

def function1():
	emptyList = []
	print(NAME)
	
	fileArr = newFunc(fileName)
	
	for x in fileArr:
		print(x)

listInt = [1,4,9,16,25,36,49,64]
listStr = ['Pele', 'Maradona', 'Zidane', 'Platini', 'Klinsmann', 'Ronaldo', 'Messi', 'Bale']
listSqrt = []

def finalFunction(listInt, listStr):
	for x in listInt:
		listSqrt.append(math.sqrt(x))
	for x in range(0, 8):
		f.write(f' {listInt[x]} {math.sqrt(listInt[x]):5}  {listStr[x]:5}\n')
		
function1()
finalFunction(listInt, listStr)
