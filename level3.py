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
    "road_sqr",
    'road_t_b_l',
    'road_t_b_r',
]

level = [
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
    [2, 2, 2, 5, 1, 0, 0, 0, 4, 2, 2, 8, 2, 2, 2],
    [0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 3, 1, 1, 1],
    [2, 2, 2, 9, 0, 1, 0, 4, 7, 0, 0, 3, 1, 1, 1],
    [0, 0, 0, 3, 1, 1, 0, 3, 1, 0, 0, 3, 1, 1, 1],
    [0, 4, 2, 8, 2, 2, 2, 8, 2, 2, 2, 8, 2, 2, 8],
    [0, 3, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0],
    [0, 3, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0],
    [0, 3, 0, 10, 2, 2, 2, 8, 2, 2, 2, 9, 0, 0, 0],
    [0, 3, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0],
]

p = Actor('player',topleft = (3*TS, 1*TS))
g = Actor("goal", topleft = (14*TS, 5*TS))
e1 = Actor('enemy',topleft=(8*TS, 5*TS))

def draw():
    screen.clear()
    for row in range(len(level)):
        for column in range(len(level[row])):
            x = column * TS
            y = row * TS
            tile = tiles[level[row][column]]
            screen.blit(tile, (x, y))

    p.draw()
    g.draw()
    e1.draw()

# add more enemy on the roads and then write logic for collision

def update():
    if e1.colliderect(p):
        p.image = 'alien_hurt'


def on_key_down(key):
    row = int(p.y / TS)
    column = int(p.x / TS)
    if key == keys.UP:
        row = row - 1
    if key == keys.DOWN:
        row = row + 1
    if key == keys.LEFT:
        column = column - 1
    if key == keys.RIGHT:
        column = column + 1
    try:
        tile = tiles[level[row][column]]
        if 'road' in tile:
            x = column * TS
            y = row * TS
            animate(p, duration=0.3, topleft=(x, y))
        else:
            print('cannot go into the woods')
    except:
        print('out of bounds')



