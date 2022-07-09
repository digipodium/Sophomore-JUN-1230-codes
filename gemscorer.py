WIDTH = 500
HEIGHT = 500
from random import randint
player = Actor("green_alien", pos=(WIDTH / 2, HEIGHT / 2))
gem = Actor("gem", pos=(randint(0, WIDTH), randint(30, HEIGHT)))
score = 0
bat = Actor("bat_flying")
is_game_over = False

def draw():
    if not is_game_over:
        screen.fill('white')
        player.draw()
        gem.draw()
        bat.draw()
        screen.draw.text(f"Score : {score}",(20,20),color='red')
    else:
        screen.fill('black')
        screen.draw.text(f"Gameover",(WIDTH/2-100,HEIGHT/2),color='red',fontsize=50,fontname='blueberry')


def update():
    global score, is_game_over

    if keyboard.right and player.right < WIDTH:
        player.x += 3
    if keyboard.left and player.left > 0:
        player.x -= 3
    if keyboard.down and player.bottom < HEIGHT:
        player.y += 3
    if keyboard.up and player.top > 0:
        player.y -= 3
    if player.colliderect(gem):
        gem.x = randint(0,WIDTH)
        gem.y = randint(30,HEIGHT)
        score += 1
        sounds.hit.play()

    # enemy chase code x axis
    if bat.x < player.x:
        bat.x += 1
    if bat.x > player.x:
        bat.x -= 1

    # enemy chase code y axis
    if bat.y < player.y:
        bat.y += 1
    if bat.y > player.y:
        bat.y -= 1
    if bat.colliderect(player):
        if not is_game_over: sounds.splat.play()
        is_game_over = True


