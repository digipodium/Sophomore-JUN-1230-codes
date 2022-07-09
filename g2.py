HEIGHT = 400
WIDTH = 600

def draw():
    screen.fill('green')
    for x in range(20,WIDTH,80):
        screen.draw.filled_circle((x,20), 30, 'yellow')

    for x in range(20,WIDTH,80):
        screen.draw.filled_circle((x,HEIGHT-30),30,'red')

    screen.draw.text("Welcome to PYGAME zero", (200,200),color='black')


