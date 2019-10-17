import math

# Create a python function which accepts a decimal 
# number and returns a hexadecimal number in the form 
# of a string. Test your function with the following 
# numbers as input 23,665 and 65,537.


def DecimalToHexidecimal(decimal_number):
    hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    new_dict = dict([(value, key) for key, value in hex_dict.items()]) 
    power = 0
    hex_number_list = []
    while decimal_number / (16**power) >= 1:
        power += 1
    power -= 1
    while power >= 0:
        if(decimal_number / (16**power) >= 1):
            x = math.floor(decimal_number / (16**power))
            decimal_number -= x*(16**power)
            power -= 1
            if x in new_dict.keys():
                hex_number_list.append(str(new_dict[x]))
        else:
            hex_number_list.append('0')
            power-=1
    return "".join(hex_number_list)

print(DecimalToHexidecimal(23665))
print(DecimalToHexidecimal(65537))