import random
def show_board(queen_locations) :
    board = [['.' for _ in range(8)] for __ in range(8)]
    board_index = 0
    while board_index < 8 :
        for row_index in range(8) :
            if row_index == queen_locations[board_index][0] :
                for col_index in range(8) :
                    if col_index == queen_locations[board_index][1] :
                        board[row_index][col_index] = str(board_index)
        board_index += 1
    for arr in board :
        row = '  '.join(arr)
        print(row)

locations = [(0,0),(6,1),(2,2),(5,3),(4,4),(7,5),(1,6),(2,6)]

show_board(locations)

def same_row(point1, point2):
    if point1[0] == point2[0]:
        return True
    else:
        return False

def same_column(point1, point2):
    if point1[1] == point2[1]:
        return True
    else:
        return False

def same_diagnol(point1, point2):
    delta_y = point2[1] - point1[1]
    delta_x = point2[0] - point1[0]
    if delta_y/delta_x == 1 or delta_y/delta_x == -1:
        return True
    else:
        return False

def calc_cost(queen_locations):
    cost = 0
    for point1 in range(len(queen_locations)):
        for point2 in range(len(queen_locations)):
            if point1 == point2:
                break
            if same_row(locations[point1], locations[point2]) or same_column(locations[point1], locations[point2]) or same_diagnol(locations[point1], locations[point2]):
                cost += 1
    return cost

print('Testing calc_cost...')
assert calc_cost(locations) == 10
print('Passed')

def random_optimizer(n):
    locations_list = [[] for space in range(n)]
    for index in range(n) :
        for tuple in range(8) :
            queen = (random.randint(0,8), random.randint(0,8))
            locations_list[index].append(queen)
    lowest_cost = calc_cost(locations_list[0])
    for location_list in locations_list :
        cost = calc_cost(location_list)
        if cost <= lowest_cost :
            lowest_cost = cost
            result_location = location_list
    return {'locations' : result_location, 'cost' : lowest_cost}


print("n = 10:" + str(random_optimizer(10)))
print("n = 50:" + str(random_optimizer(50)))
print("n = 100:" + str(random_optimizer(100)))
print("n = 500:" + str(random_optimizer(500)))
print("n = 1000:" + str(random_optimizer(1000)))