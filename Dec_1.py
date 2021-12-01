with open('Dec_1.txt', 'r') as infile:
    input = infile.readlines()

new_list = []
for x in input:
    x = int(x)
    new_list.append(x)

increase = 0
index = 0
for x in new_list:
    if x > new_list[index - 1]:
        increase += 1
    index += 1

print(increase)
