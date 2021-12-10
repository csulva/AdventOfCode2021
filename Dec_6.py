import statistics

days = 80
input = [3,4,3,1,2]
total_length_after_each_day = []
def calculate_lanternfish_total(input, days):
    while days > 0:
        for i in range(len(input)):
            input[i] -= 1
            if input[i] == -1:
                input[i] = 6
                input.append(8)
        # total_length_after_each_day.append(len(input))
        days -= 1
    return len(input)

input = [3,4,3,1,2]
my_input = [1,5,5,1,5,1,5,3,1,3,2,4,3,4,1,1,3,5,4,4,2,1,2,1,2,1,2,1,5,2,1,5,1,2,2,1,5,5,5,1,1,1,5,1,3,4,5,1,2,2,5,5,3,4,5,4,4,1,4,5,3,4,4,5,2,4,2,2,1,3,4,3,2,3,4,1,4,4,4,5,1,3,4,2,5,4,5,3,1,4,1,1,1,2,4,2,1,5,1,4,5,3,3,4,1,1,4,3,4,1,1,1,5,4,3,5,2,4,1,1,2,3,2,4,4,3,3,5,3,1,4,5,5,4,3,3,5,1,5,3,5,2,5,1,5,5,2,3,3,1,1,2,2,4,3,1,5,1,1,3,1,4,1,2,3,5,5,1,2,3,4,3,4,1,1,5,5,3,3,4,5,1,1,4,1,4,1,3,5,5,1,4,3,1,3,5,5,5,5,5,2,2,1,2,4,1,5,3,3,5,4,5,4,1,5,1,5,1,2,5,4,5,5,3,2,2,2,5,4,4,3,3,1,4,1,2,3,1,5,4,5,3,4,1,1,2,2,1,2,5,1,1,1,5,4,5,2,1,4,4,1,1,3,3,1,3,2,1,5,2,3,4,5,3,5,4,3,1,3,5,5,5,5,2,1,1,4,2,5,1,5,1,3,4,3,5,5,1,4,3]
# print(calculate_lanternfish_total(input, 80))

growth_numbers_after_80_days = [5, 6, 7, 9, 10, 10, 10, 10, 11, 12, 15, 17, 19, 20, 20, 21, 22, 26, 29, 34, 37, 39, 41, 42, 47, 51, 60, 66, 73, 78, 81, 88, 93, 107, 117, 133, 144, 154, 166, 174, 195, 210, 240, 261, 287, 310, 328, 361, 384, 435, 471, 527, 571, 615, 671, 712, 796, 855, 962, 1042, 1142, 1242, 1327, 1467, 1567, 1758, 1897, 2104, 2284, 2469, 2709, 2894, 3225, 3464, 3862, 4181, 4573, 4993, 5363, 5934]

# print(calculate_lanternfish_total(my_input, 2))
# print(calculate_lanternfish_total(my_input, 4))
# print(calculate_lanternfish_total(my_input, 16))
print(len(my_input))

def growth(list):

   # new list for growth rates
    growth_rate = []

   # for population in list
    for pop in range(1, len(list)):

       gnumbers = ((list[pop] - list[pop-1]) * 100 / list[pop-1])
       growth_rate.append(gnumbers)
    return growth_rate

print(statistics.fmean(growth(growth_numbers_after_80_days)))

initial_amount = float(300(1 + 9.476848772455204) ** 8)
print(initial_amount)