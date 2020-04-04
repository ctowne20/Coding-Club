# Python Coding Club
# Assignment 4- Classes
# April 9, 2020
# Carrieann Towne

# LTU Honor Code: "I have neither given nor received unauthorized aid in 
#	completing this work, nor have I presented someone else's work as my own."
	
class Students: 
	def __init__(self, firstName, lastName, email, gpa):
		self.firstName = firstName
		self.lastName = lastName
		self.email = email
		self.gpa = gpa
		
	def FullDetails(self):
		return '{} {}, GPA: {}'.format(self.firstName, self.lastName, self.gpa)
		
class Enrollment(Students):
	def __init__(self, firstName, lastName, email, gpa, sectionName, sectionNumber, credits):
		super().__init__(firstName, lastName, email, gpa)		
		self.sectionName = sectionName
		self.sectionNumber = sectionNumber
		self.credits = credits
		
	def MoreDetails(self):
		return self.FullDetails() + ", Section: " + self.sectionName
		
student1 = Students('Carrieann', 'Towne', 'ctowne@ltu.edu', 3.89)
student2 = Students('Mitchell', 'Pleune', 'mpleune@ltu.edu', 3.79)
student3 = Enrollment('Isabel', 'Fiori', 'ifiori@ltu.edu', 3.23, 'Basic Design III', 3772, 6)
student4 = Enrollment('Brandon', 'Kane', 'bkane@ltu.edu', 3.57, 'Fluids', 4839, 4)

print(student1.FullDetails())
print(student2.FullDetails())
print(student3.MoreDetails())
print(student4.MoreDetails())