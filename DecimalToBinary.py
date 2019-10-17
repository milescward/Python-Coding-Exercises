# Create a python function which accepts a decimal number and 
# returns a binary number in the form of a string. Test your
# function with the following numbers as input 87 and 65,537.

def DecimalToBinary(decimal_number):
    power = 0
    binary_number_list = []
    while decimal_number / (2**power) >= 1:
        power += 1
    power -= 1
    while power >= 0:
        if(decimal_number / (2**power) >= 1):
            binary_number_list.append('1')
            decimal_number -= 2**power
            power -= 1
        else:
            binary_number_list.append('0')
            power -= 1
    return "".join(binary_number_list)

#print(DecimalToBinary(65537))