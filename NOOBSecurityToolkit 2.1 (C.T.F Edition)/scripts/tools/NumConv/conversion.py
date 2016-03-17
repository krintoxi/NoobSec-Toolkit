# Functions for Conversions

letToNum = {
	"0": 0,
	"1": 1,
	"2": 2, 
	"3": 3, 
	"4": 4, 
	"5": 5, 
	"6": 6, 
	"7": 7, 
	"8": 8, 
	"9": 9, 
	"A": 10, 
	"B": 11, 
	"C": 12, 
	"D": 13, 
	"E": 14, 
	"F": 15,
	"G": 16, 
	"H": 17, 
	"I": 18, 
	"J": 19, 
	"K": 20, 
	"L": 21, 
	"M": 22, 
	"N": 23, 
	"O": 24, 
	"P": 25, 
	"Q": 26,
	"R": 27,
	"S": 28,
	"T": 29,
	"U": 30,
	"V": 31,
	"W": 32,
	"X": 33,
	"Y": 34,
	"Z": 35
 }

numToLet = {
	0: "0",
	1: "1", 
	2: "2", 
	3: "3", 
	4: "4", 
	5: "5", 
	6: "6", 
	7: "7", 
	8: "8", 
	9: "9", 
	10: "A", 
	11: "B", 
	12: "C", 
	13: "D", 
	14: "E", 
	15: "F",
	16: "G",
	17: "H",
	18: "I",
	19: "J",
	20: "K",
	21: "L",
	22: "M",
	23: "N",
	24: "O",
	25: "P",
	26: "Q",
	27: "R",
	28: "S",
	29: "T",
	30: "U",
	31: "V",
	32: "W",
	33: "X",
	34: "Y",
	35: "Z",
	}


def fromDenary(num, base):
	# Make sure arguments are Integers
	num = int(num) 
	base = int(base)
	print( num, base)
	div = -1
	remainder = 0 # Remainder variable
	remainders = []
	baseString = ""
	while div != 0:
		div = num // base
		print (div)
		remainder = num % base
		print (remainder)
		newRemainder = numToLet[remainder]
		remainders.append(newRemainder)
		num = div
	for item in remainders:
		baseString = item + baseString
	return baseString

def toDenary(num, base):
	# Make sure num is a String
	num = str(num) 
	# Make sure base is Integer
	base = int(base)

	length = len(num) # 
	i = length - 1
	total = 0
	baseCounter = 0
	while i >= 0:
		value = num[i]
		if value != "0":
			numValue = letToNum[value] * (base ** baseCounter)
		else:
			numValue = 0
		total = total + numValue
		i = i - 1
		baseCounter += 1
	return total
