import random
import pygame

pygame.init()

WIDTH = 900
HEIGHT = 500
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
red = (255, 0, 0)
yellow = (255, 255, 0)
fps = 60
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Alien Boy')
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)
mode = 0  # mode 0 = idle, 1 = right, 2 = left, 3 = jumping, 4 = crouching
frames = ['assets/idle1.png', 'assets/idle2.png', 'assets/crouch.png', 'assets/jump.png', 'assets/right1.png', \
          'assets/right2.png', 'assets/left1.png', 'assets/left2.png']
active = 0
count = 0
player_x = 200
player_y = 200
x_speed = 3
y_change = 0
gravity = .4
in_air = False


def update_player(mod, counter):
    if counter >= 60:
        counter = 0
    if mod == 0:
        if counter < 30:
            act = 0
        elif 30 <= counter < 60:
            act = 1
    if mod == 1:
        if counter < 30:
            act = 4
        elif 30 <= counter < 60:
            act = 5
    if mod == 2:
        if counter < 30:
            act = 6
        elif 30 <= counter < 60:
            act = 7
    if mod == 3:
        act = 3
    if mod == 4:
        act = 2
    counter += 1
    return act, counter


running = True
while running:
    timer.tick(fps)
    screen.fill(gray)
    floor = pygame.draw.rect(screen, white, [0, 300, WIDTH, HEIGHT - 300])
    floor_line = pygame.draw.line(screen, black, (0, 300), (WIDTH, 300), 5)
    active, count = update_player(mode, count)
    player = pygame.transform.scale(pygame.image.load(frames[active]), (150, 150))
    screen.blit(player, (player_x, player_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and not in_air:
                mode = 1
            elif event.key == pygame.K_LEFT and not in_air:
                mode = 2
            elif event.key == pygame.K_DOWN:
                mode = 4
            elif event.key == pygame.K_SPACE and not in_air:
                in_air = True
                y_change = -10
                mode = 3
            else:
                mode = 0
        if event.type == pygame.KEYUP and mode != 0 and not in_air:
            mode = 0

    if mode == 1:
        if player_x + x_speed + 120 < WIDTH:
            player_x += x_speed
    elif mode == 2:
        if player_x - x_speed + 30 > 0:
            player_x -= x_speed

    player_y += y_change
    if in_air:
        y_change += gravity
    if player_y > 200:
        player_y = 200
        y_change = 0
        in_air = False
        mode = 0

    pygame.display.flip()
pygame.quit()
