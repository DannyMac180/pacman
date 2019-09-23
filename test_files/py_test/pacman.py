"""
Returns the final_pos_x, final_pos_y, and coins_colected of a pacman.
"""

__author__ = "Dan McAteer"

def read_input(text_file):

    input_file = open(text_file)
    lines = input_file.readlines()

    return lines

def get_grid_size(input_arr):

    line_1 = input_arr[0]
    x_coord, y_coord = map(int, line_1.split(" "))

    return x_coord, y_coord

def get_grid_perim(input_arr):

    grid_size = get_grid_size(input_arr)
    perim = []

    for index in range(0, grid_size[0]):
        x_perim_lower = (index, 0)
        x_perim_upper = (index, grid_size[1])
        y_perim_left = (0, index)
        y_perim_right = (grid_size[0], index)

        perim += [x_perim_lower, x_perim_upper, y_perim_left, y_perim_right]

    return perim

def get_start_pos(input_arr):

    line_2 = input_arr[1]
    x_coord, y_coord = map(int, line_2.split(" "))

    return x_coord, y_coord

def get_walls(input_arr):

    walls = []
    
    for index in range(3, len(input_arr)):
        
        line = input_arr[index]
        x_coord, y_coord = map(int, line.split(" "))
        coords = x_coord, y_coord
        walls.append(coords)
    
    return walls

def get_move_value(direction):

    direction_dict = {"N": 1, "E": 1, "S": -1, "W": -1}

    return direction_dict[direction]

def make_move(move, pos):
    x_moves = ["E", "W"]
    
    if move in x_moves:
       pos = (pos[0] + get_move_value(move)), pos[1]
    else:
       pos = pos[0], (pos[1] + get_move_value(move))
    
    return pos

def stop_move(move, pos):
    x_moves = ["E", "W"]

    if move in x_moves:
        pos = (pos[0] - get_move_value(move)), pos[1]
    else:
        pos = pos[0], (pos[1] - get_move_value(move))

    return pos

def is_edge_case(start_pos, grid_size, walls, moves):

    if start_pos > grid_size:
        return True
    elif start_pos in walls:
        return True
    elif not all(elem in ['N', 'S', 'E', 'W'] for elem in moves):
        return True
    else:
        return False
    
def pacman(input_file):
    """ Use this function to format your input/output arguments. Be sure not to change the order of the output arguments. 
    Remember that code organization is very important to us, so we encourage the use of helper fuctions and classes as you see fit.
    
    Input:
        1. input_file (String) = contains the name of a text file you need to read that is in the same directory, includes the ".txt" extension
           (ie. "input.txt")
    Outputs:
        1. final_pos_x (int) = final x location of Pacman
        2. final_pos_y (int) = final y location of Pacman
        3. coins_collected (int) = the number of coins that have been collected by Pacman across all movements
    """
    input_arr = read_input(input_file)
    grid_size = get_grid_size(input_arr)
    grid_perim = get_grid_perim(input_arr)
    start_pos = get_start_pos(input_arr)
    walls = get_walls(input_arr)
    moves = input_arr[2].strip()
    coins_collected = 0
    traversed_points = [start_pos]

    if is_edge_case(start_pos, grid_size, walls, moves):
        return (-1, -1, 0)

    for move in moves:

        start_pos = make_move(move, start_pos)

        if start_pos in walls or start_pos in grid_perim:
            start_pos = stop_move(move, start_pos)
        elif start_pos in traversed_points:
            continue
        else:
            coins_collected += 1

        traversed_points.append(start_pos)

    final_pos_x = start_pos[0]
    final_pos_y = start_pos[1]
    return final_pos_x, final_pos_y, coins_collected