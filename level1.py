TS = 64

WIDTH = TS * 12
HEIGHT = TS * 10

tiles = ["medieval_trees", "medieval_grass_2", "medieval_grass"]

maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 2],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 2, 2],
    [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 2, 2],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 2, 2],
    [0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 2, 2],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
]


def draw():
    screen.clear()
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * TS
            y = row * TS
            tile = tiles[maze[row][column]]
            screen.blit(tile, (x, y))
