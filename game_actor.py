WIDTH = 800
HEIGHT = 500

alien = Actor('alien',bottomright=(WIDTH,HEIGHT))
alien2 = Actor('alien',topright=(WIDTH,0))
alien3 = Actor('alien',bottomleft=(0,HEIGHT))
alien4 = Actor('alien',center=(WIDTH/2, HEIGHT/2))
bg = Actor('background')


def draw():
    screen.fill('black')
    bg.draw()
    screen.draw.text("Game Actors",(20,20),fontsize=30,color='red')
    alien.draw()
    alien2.draw()
    alien3.draw()
    alien4.draw()

def update():
    # Right to left
    alien.x += -2
    if alien.x < 0:
        alien.x = WIDTH

    # Right to left
    alien2.x += -1
    if alien2.x < 0:
        alien2.x = WIDTH

    # Left to Right



