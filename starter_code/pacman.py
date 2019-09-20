"""
Returns the final_pos_x, final_pos_y, and coins_colected of a pacman
"""
import os

__author__ = "Dan McAteer"
file_path = "test_files\py_test\generic.txt"


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
    input_arr = read_input(file_path)
    grid_size = get_grid_size(input_arr)
    start_pos = get_start_pos(input_arr)
    walls = get_walls()
    coins_collected = 0
    final_pos_x = start_pos[0]
    final_pos_y = start_pos[1]

    return final_pos_x, final_pos_y, coins_collected

def read_input(text_file):

    input_file = open(text_file, 'r')
    lines = input_file.readlines()

    return lines

def get_grid_size(input_arr):

    line_1 = input_arr[0]
    x_coord, y_coord = map(int, line_1.split(" "))

    return x_coord, y_coord

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




