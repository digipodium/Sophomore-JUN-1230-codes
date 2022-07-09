HEIGHT = 500
WIDTH = 600

bg = Actor('background')
alien = Actor('alien',topright=(WIDTH,0))
bunny = Actor('bunny1_ready',pos=(300,300))

def draw():
    bg.draw()
    screen.draw.text('example 2',(10,10),fontsize=40,color='red')
    alien.draw()
    bunny.draw()

def update():
    alien.x += 2
    alien.y += 2
    if alien.x > WIDTH:
        alien.x = 0
    if alien.y > HEIGHT:
        alien.y = 0
