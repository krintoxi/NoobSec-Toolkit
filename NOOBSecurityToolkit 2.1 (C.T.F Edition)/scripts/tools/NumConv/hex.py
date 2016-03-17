# Functions for Binary Conversions

hexToDen = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
denToHex = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

def toHex(num):
	num = int(num) # Make sure argument is an Intger
	div = -1
	mod = 0
	remainders = []
	hexString = ""
	while div != 0:
		div = num / 16
		mod = num % 16
		mod = denToHex[mod]
		remainders.append(mod)
		num = div
	for item in remainders:
		hexString = item + hexString
	return hexString

def toDenary(num):
	num = str(num) # Make sure argument is a String
	length = len(num) # Convert to binary literal
	i = length - 1
	total = 0
	hexCounter = 0
	while i >= 0:
		value = num[i]
		value = hexLetters[value] * (16 ** hexCounter)
		total = total + value
		i = i - 1
		hexCounter += 1
	return total
