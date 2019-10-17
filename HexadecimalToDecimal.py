# Create a python function which accepts a hexadecimal 
# number in the form of a string and returns a decimal 
# value. Test your function with the following strings 
# as input "54AE7" and "23FF".


def HexidecimalToDecimal(hex_num):
    hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    inter_list = []
    total = 0
    position = 0
    for item in hex_num:
        if item in hex_dict.keys():
            inter_list.append(hex_dict[item])
    for item in reversed(inter_list):
        total += item*(16**position)
        position += 1
    return total

print(HexidecimalToDecimal("23FF"))