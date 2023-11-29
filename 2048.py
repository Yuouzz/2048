import pygame
import random
import copy
import sys
board_ini = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
score = 0
color_dict = {
    2:      "#eee4da", 4:      "#ede0c8", 8:      "#f2b179", 16:     "#f59563",
    32:     "#f67c5f", 64:     "#f65e3b", 128:    "#edcf72", 256:    "#edcc61",
    512:    "#edc850", 1024:   "#edc53f", 2048:   "#edc22e", 4096:   "#eee4da",
    8192:   "#edc22e", 16384:  "#f2b179", 32768:  "#f59563", 65536:  "#f67c5f"}


def left(_board):
    _board_temp = copy.deepcopy(_board)
    for line in list(_board_temp):
        len_line = len(line)
        while 0 in line:
            line.remove(0)
        if len(line) > 0:
            for _i in range(len(line)):
                if _i < len(line) - 1 and line[_i] == line[_i+1]:
                    line[_i] = line[_i] + line[_i+1]
                    line[_i+1] = 0
                    global score
                    score += line[_i]
        while 0 in line:
            line.remove(0)
        while len(line) < len_line:
            line.append(0)
    if _board != _board_temp:
        _board_temp = generate_random(_board_temp)
    return _board_temp
