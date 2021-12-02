# Calculate the horizontal position and depth you would have after following the planned course.
# What do you get if you multiply your final horizontal position by your final depth?

with open('Dec_2.txt', 'r') as infile:
    input = infile.readlines()

new_list = []
for x in input:
    string = x.split()
    new_list.append(string)

# print(new_list)

list_2 = []
for x in new_list:
    x[1] = int(x[1])
    list_2.append(x)

def calculate_position(lists):
    horizontal = 0
    depth = 0
    for x in lists:
        if x[0] == 'forward':
            horizontal += x[1]
        if x[0] == 'up':
            depth -= x[1]
        if x[0] == 'down':
            depth += x[1]
    position = horizontal * depth
    return position

test_list = [['forward', 5], ['down', 5], ['forward', 8], ['up', 3], ['down', 8], ['forward', 2]]

print(calculate_position(test_list))
print(calculate_position(list_2))

# Using this new interpretation of the commands, calculate the horizontal position
# and depth you would have after following the planned course.
# What do you get if you multiply your final horizontal position by your final depth?

def calculate_position(lists):
    horizontal = 0
    depth = 0
    aim = 0
    for x in lists:
        if x[0] == 'forward':
            horizontal += x[1]
            depth += aim * x[1]
        if x[0] == 'up':
            aim -= x[1]
        if x[0] == 'down':
            aim += x[1]
    position = horizontal * depth
    return position

print(calculate_position(list_2))