with open('Dec_4.txt', 'r') as infile:
    input = infile.readlines()

with open('Dec_4_boards.txt', 'r') as infile:
    boards = infile.readlines()

for x in input:
    x = x.split(',')
    new_list = []
    for y in x:
        new_list.append(y.strip())

# new_list is list of input strings to use
# print(new_list)
new_boards = []
for x in boards:
    new_boards.append(x.strip())
# print(new_boards)

index = 0
board_list = []
new_listy = []
for x in new_boards:
    x = x.split(' ')
    if '' in x:
        x.remove('')
        new_listy.append(x)
    else:
        new_listy.append(x)
    index += 1
    if len(new_listy) == 5:
        board_list.append(new_listy)
    # if index == 25:
        # board_list.append(new_list)
        index == 0

for lists in board_list[0]:
    if lists == []:
        board_list[0].remove(lists)
# ints = [int(z) for z in board_list[0][0]]
# if [type(int) is int for int in ints]:
#     print(ints)

row = 0
column = 0
columns_list = []
columns = []
index = 0
while column < 5:
    for x in board_list[0]:
        column_num = board_list[0][row][column]
        columns.append(column_num)
        row += 1
        if row % 5 == 0:
            columns_list.append(columns)
            columns = []
            if row >= 500:
                row = 0
                column += 1
                # if column >= 5:
                # column = 0

def check_boards(input_list, board_lists):
    removed_list = set()
    count = 1
    for x in input_list:
        for y in board_lists[0]:
            for num in y:
                if num == x:
                    y.remove(num)
                    removed_list.add(num)
                    if y == []:
                        print('number:' + num)
                        print('count:' + str(count))
                        print(f'discarded: {removed_list}')
                        quit()
                continue
        count += 1

                    # for the_row in board_lists[0]:
                    #     ints = [z for z in the_row]
                    #     if [type(int) is int for int in ints]:
                    #         print(ints)
                    #         print(num)

test_input = ['7','4','9','5','11','17','23','2','0','14','21','24','10','16','13','6','15','25','12','22','18','20','8','19','3','26','1']
test_board = [['22', '13', '17', '11', '0'],
['8', '2', '23', '4', '24'],
['21', '9', '14', '16', '7'],
['6', '10', '3', '18', '5'],
['1', '12', '20', '15', '19'],
['3', '15', '0', '2', '22'],
['9', '18', '13', '17', '5'],
['19', '8', '7', '25', '23'],
['20', '11', '10', '24', '4'],
['14', '21', '16', '12', '6'],
['14', '21', '17', '24', '4'],
['10', '16', '15', '9', '19'],
['18', '8', '23', '26', '20'],
['22', '11', '13', '6', '5'],
['2', '0', '12', '3', '7']]

# check_boards(test_input, test_board)
# print(new_list)
# print(board_list)
# print(columns_list)

# check_boards(new_list, columns_list)
# # OUTPUT number:7
# count:20
# discarded: {'21', '1', '2', '55', '48', '62', '36', '63', '94', '58', '6', '16', '47', '92', '44', '40', '7', '17', '20', '4'}
check_boards(new_list, board_list)