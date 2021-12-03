# Use the binary numbers in your diagnostic report to calculate the gamma rate
# and epsilon rate, then multiply them together.
# What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

with open('Dec_3.txt', 'r') as infile:
    input = infile.readlines()

new_input = []
for x in input:
    new_input.append(x.strip())

def gamma(list):
    list_1 = []
    index = 0
    while index < len(list[0]):
        zero = 0
        one = 0
        for bit in list:
            if bit[index] == '0':
                zero += 1
            elif bit[index] == '1':
                one += 1
        index += 1
        if zero > one:
            list_1.append(0)
        elif one > zero:
            list_1.append(1)
    return list_1

def epsilon(list):
    list_1 = []
    index = 0
    while index < len(list[0]):
        zero = 0
        one = 0
        for bit in list:
            if bit[index] == '0':
                one += 1
            elif bit[index] == '1':
                zero += 1
        index += 1
        if zero > one:
            list_1.append(0)
        elif one > zero:
            list_1.append(1)
    return list_1

test_list = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010','01010']
# print(gamma(test_list))
# # Output 10110 or 22 in decimal
# print(epsilon(test_list))
# # Output 01001 or 9 in decimal

print(gamma(new_input))
# Output 10110 or 22 in decimal
print(epsilon(new_input))
# Output 01001 or 9 in decimal
gamma_rate = 2635
epsilon_rate = 1460
print(gamma_rate * epsilon_rate)

# Part two

# Use the binary numbers in your diagnostic report to calculate the oxygen generator 
# rating and CO2 scrubber rating, then multiply them together. 
# What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)

def oxygen(list):

    index = 0
    while len(list) > 1:
        zero = 0
        one = 0
        for x in list:
            if x[index] == '0':
                zero += 1
            if x[index] == '1':
                one += 1
        if one >= zero:
            list = [x for x in list if x[index] == '1']
        elif one < zero:
            list = [x for x in list if x[index] == '0']
        index += 1
    return list

def c02(list):

    index = 0
    while len(list) > 1:
        zero = 0
        one = 0
        for x in list:
            if x[index] == '0':
                zero += 1
            if x[index] == '1':
                one += 1
        if zero > one:
            list = [x for x in list if x[index] == '1']
        elif zero <= one:
            list = [x for x in list if x[index] == '0']
        index += 1
    return list

print(oxygen(new_input))
# Output = 101010101111 or 2735
print(c02(new_input))
# Output = 010111011101 or 1501

oxygen_rate = 2735
c02_rate = 1501
print(oxygen_rate * c02_rate)
