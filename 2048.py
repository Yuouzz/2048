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


def right(_board):
    for _i in range(len(_board)):
        _board[_i].reverse()
    _board = left(_board)
    for _i in range(len(_board)):
        _board[_i].reverse()
    return _board


def up(_board):
    _board_temp = copy.deepcopy(board_ini)
    for _i in range(len(_board)):
        for j in range(len(_board)):
            _board_temp[j][_i] = _board[_i][j]
    _board_temp = left(_board_temp)
    for _i in range(len(_board)):
        for j in range(len(_board)):
            _board[_i][j] = _board_temp[j][_i]
    return _board


def down(_board):
    _board.reverse()
    _board = up(_board)
    _board.reverse()
    return _board


def generate_random(_board):
    _zero = [(x, y) for x in range(len(_board)) for y in range(len(_board)) if _board[x][y] == 0]
    if _zero:
        x, y = random.choice(_zero)
        _board[x][y] = random.choice([2, 2, 2, 4])
    return _board


def display_board(_board):
    screen.fill(color='#6b5f52')
    _background = pygame.Surface((290, 290))
    _background.fill(color='#dbb067')
    screen.blit(_background, (70, 70))
    cells = [(x, y) for x in range(len(board)) for y in range(len(board))]
    for i in cells:
        x, y = tuple(i)
        num = board[x][y]
        _display_x = 100 + 60 * y
        _display_y = 100 + 60 * x
        _self_block = pygame.Surface((50, 50))
        if num == 0:
            _self_block.fill(color='#ddceb3')
            screen.blit(_self_block, (_display_x, _display_y))
        else:
            _self_block.fill(color=color_dict[num])
            screen.blit(_self_block, (_display_x, _display_y))
            text = f.render(str(num), True, 'black')
            text_position = text.get_rect()
            text_position.center = (_display_x + 25, _display_y + 25)
            screen.blit(text, text_position)
    score_text = f.render("Score:" + str(score), True, 'white')
    screen.blit(score_text, (10, 10))
    pygame.display.flip()


def board_init():
    _board = copy.deepcopy(board_ini)
    _board = generate_random(_board)
    _board = generate_random(_board)
    return _board


pygame.init()
screen = pygame.display.set_mode((400, 400))
f = pygame.font.SysFont(['Tahoma'], 25)
board = board_init()
board_old = copy.deepcopy(board)
score_old = 0
state = True
display_board(board)
while state:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            board_old_temp = copy.deepcopy(board)
            score_old_temp = score
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                board = up(board)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                board = left(board)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                board = down(board)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                board = right(board)
            elif event.key == pygame.K_r:
                board = board_init()
                score = 0
            elif event.key == pygame.K_x:
                board = copy.deepcopy(board_old)
                score = score_old
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if board != board_old_temp:
                board_old = board_old_temp
                score_old = score_old_temp
            display_board(board)

