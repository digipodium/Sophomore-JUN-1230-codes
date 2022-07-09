WIDTH = 500
HEIGHT = 500

alien = Actor("green_alien", pos=(WIDTH / 2, HEIGHT / 2))
bat = Actor("bat_flying")

def draw():
    screen.fill("black")
    alien.draw()
    bat.draw()

def update():
    if keyboard.left:
        alien.x -= 3
    if keyboard.right:
        alien.x += 3
    if keyboard.up:
        alien.y -= 3
    if keyboard.down:
        alien.y += 3

    # enemy chase code x axis
    if bat.x < alien.x:
        bat.x += 1
    if bat.x > alien.x:
        bat.x -= 1

    # enemy chase code y axis
    if bat.y < alien.y:
        bat.y += 1
    if bat.y > alien.y:
        bat.y -= 1
