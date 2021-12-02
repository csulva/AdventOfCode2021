# Part 1
# How many measurements are larger than the previous measurement?

with open('Dec_1.txt', 'r') as infile:
    input = infile.readlines()

# Converting to ints
new_list = []
for x in input:
    x = int(x)
    new_list.append(x)

increase = 0
index = 0
for x in new_list:
    if index - 1 < 0:
        pass
    if x > new_list[index - 1]:
        increase += 1
    index += 1

print(increase)

# Part 2
# Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

index = 0
list_of_sum = []
for x in new_list:
    sum = new_list[index] + new_list[index + 1] + new_list[index + 2]
    list_of_sum.append(sum)
    index += 1
    if index == len(new_list) - 2:
        break

increase = 0
index = 0
for x in list_of_sum:
    if x > list_of_sum[index - 1]:
        increase += 1
    index += 1

print(increase)