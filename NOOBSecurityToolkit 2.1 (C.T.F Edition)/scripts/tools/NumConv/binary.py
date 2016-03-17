# Functions for Binary Conversions

def toBinary(num):
	num = int(num) # Make sure argument is an Intger
	binary = bin(num) # Convert to binary literal
	binary = binary[2:] # Remove first 2 chars 0b to format it
	binary = int(binary) # Convert literal to int
	return binary 

def toDenary(num):
	denary = int(num, 2)
	return denary

