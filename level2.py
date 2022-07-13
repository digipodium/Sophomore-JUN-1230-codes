TS = 64

HEIGHT = TS * 10
WIDTH = TS * 15

tiles = [
    "grass",
    "tree_3",
    "road_hor",
    "road_vert",
    "road_b_r",
    "road_b_l",
    "road_t_r",
    "road_t_l",
]

level = [
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
    [2, 2, 2, 5, 1, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2],
    [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def draw():
    screen.clear()
    for row in range(len(level)):
        for column in range(len(level[row])):
            x = column * TS
            y = row * TS
            tile = tiles[level[row][column]]
            screen.blit(tile, (x, y))
