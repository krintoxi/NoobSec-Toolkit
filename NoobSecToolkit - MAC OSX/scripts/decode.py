import math

def bin_to_dec(binary):
    binary = binary[2:]
    result = 0
    for i in range(len(binary)):
        result += 2 ** (len(binary) - i - 1) * int(binary[i])
    return str(result)

def dec_to_bin(decimal):
    result = ""
    power = int(math.log2(float(decimal)))
    decimal = int(decimal)
    while power >= 0:
        if 2 ** power <= decimal:
            decimal -= 2 ** power
            result += "1"
        else:
            result += "0"
        power -= 1
    return "0b" + result

hex_to_bin_map = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "a": "1010", "b": "1011", "c": "1100", "d": "1101", "e": "1110", "f": "1111"}
bin_to_hex_map = {hex_to_bin_map[x]: x for x in hex_to_bin_map.keys()}

def hex_to_bin(hexadecimal):
    hexadecimal = hexadecimal[2:]
    result = ""
    for digit in hexadecimal:
        result += hex_to_bin_map[digit]
    return "0b" + result

def bin_to_hex(binary):
    binary = binary[2:]
    binary = "0" * (-len(binary) % 4) + binary
    result = ""
    for i in range(0, len(binary), 4):
        result += bin_to_hex_map[binary[i:i+4]]
    return "0x" + result

def hex_to_dec(hexadecimal):
    return bin_to_dec(hex_to_bin(hexadecimal))

def dec_to_hex(decimal):
    return bin_to_hex(dec_to_bin(decimal))


while True:
    to_convert = str.lower(input(""))

    if len(to_convert) > 2 and to_convert[:2] == "0b":
        print(bin_to_hex(to_convert))
        print(bin_to_dec(to_convert))
    elif len(to_convert) > 2 and to_convert[:2] == "0x":
        print(hex_to_bin(to_convert))
        print(hex_to_dec(to_convert))
    else:
        print(dec_to_bin(to_convert))
        print(dec_to_hex(to_convert))

    print("")

