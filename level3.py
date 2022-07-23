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

gems = []
total_gems = 5
collected_gems = 0
gems_coordinates = [(7,1),(8,5),(1,11),(5,9),(2,8)]

level_complete = False
game_over = False

score = 0

for x,y in gems_coordinates:
    gem = Actor('gold_1', topleft = (y*TS, x*TS))
    gems.append(gem)

def draw():
    screen.clear()
    if game_over:
        screen.blit('background',pos=(0,0))
        screen.draw.text('GAME\nOVER',(50,50),color='white',fontsize=100)
    elif level_complete:
        screen.fill('green')
        screen.draw.text('LEVEL COMPLETE',(50,50),color='white',fontsize=100)
    else:
        for row in range(len(level)):
            for column in range(len(level[row])):
                x = column * TS
                y = row * TS
                tile = tiles[level[row][column]]
                screen.blit(tile, (x, y))

        p.draw()
        g.draw()
        e1.draw()
        for gem in gems:
            gem.draw()

        screen.draw.text(f'score: {score}', (20,20), color='red',fontsize=40)
        screen.draw.text(f'coins left: {total_gems - collected_gems}',(20,50), color='red',fontsize=40)

# add more enemy on the roads and then write logic for collision

def update():
    global collected_gems,score,game_over,level_complete

    if not game_over and not level_complete:
        if e1.colliderect(p):
            p.image = 'alien_hurt'
            game_over = True

        for idx, gem in enumerate(gems):
            if p.colliderect(gem):
                gems.pop(idx)
                score += 100
                collected_gems +=1

        if p.colliderect(g):
            if collected_gems == total_gems:
                print("level complete")
                level_complete = True


def on_key_down(key):
    if not game_over and not level_complete:
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



