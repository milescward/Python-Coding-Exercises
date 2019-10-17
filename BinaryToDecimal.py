import math

# Create a python function which accepts a binary number in the form 
# of a string and returns a decimal value. Test your function with 
# the following strings as input "1100110101" and "1010101011".
def BinaryToDecimal(binary_number):
    binary_number_list = []
    total = 0
    position = 0
    for item in binary_number:
        binary_number_list.append(int(item))
    for item in reversed(binary_number_list):
        total += item*(2**position)
        position += 1
    return total

#print(BinaryToDecimal("1100110101"))






