# on your mark, get set, go!
# Breakout Edition - started 1:42 PM - done at 2:35 PM!

import pygame
import random

pygame.init()

timer = pygame.time.Clock()
fps = 60
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
red = (255, 0, 0)
orange = (255, 128, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
player_speed = 8
WIDTH = 500
HEIGHT = 900
player_x = 190
player_direction = 0
ball_x = WIDTH / 2
ball_y = HEIGHT - 30
ball_x_direction = 0
ball_y_direction = 0
ball_x_speed = 5
ball_y_speed = 5
'''board = [[5, 5, 5, 5, 5], [4, 4, 4, 4, 4], [3, 3, 3, 3, 3], [2, 2, 2, 2, 2], [1, 1, 1, 1, 1]]'''
board = []
create_new = True
colors = [red, orange, green, blue, purple]
screen = pygame.display.set_mode([WIDTH, HEIGHT])
active = False
score = 0

font = pygame.font.Font('freesansbold.ttf', 30)


def create_new_board():
    board = []
    rows = random.randint(4, 8)
    for i in range(rows):
        row = []
        for j in range(5):
            row.append(random.randint(1, 5))
        board.append(row)
    return board


def draw_board(board):
    board_squares = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                piece = pygame.draw.rect(screen, colors[(board[i][j]) - 1], [j * 100, i * 40, 98, 38], 0, 5)
                pygame.draw.rect(screen, black, [j * 100, i * 40, 98, 38], 5, 5)
                top = pygame.rect.Rect((j * 100, i * 40), (98, 1))
                bot = pygame.rect.Rect((j * 100, (i * 40) + 37), (98, 1))
                left = pygame.rect.Rect((j * 100, i * 40), (37, 1))
                right = pygame.rect.Rect(((j * 100) + 97, i * 40), (37, 1))
                board_squares.append([top, bot, left, right, (i, j)])
    return board_squares


run = True
while run:
    screen.fill(gray)
    timer.tick(fps)
    if create_new:
        board = create_new_board()
        create_new = False
    squares = draw_board(board)
    player = pygame.draw.rect(screen, black, [player_x, HEIGHT - 20, 120, 15], 0, 3)
    pygame.draw.rect(screen, white, [player_x + 5, HEIGHT - 18, 110, 11], 3, 3)
    ball = pygame.draw.circle(screen, white, (ball_x, ball_y), 10)
    pygame.draw.circle(screen, black, (ball_x, ball_y), 10, 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not active:
                active = True
                ball_y_direction = -1
                ball_x_direction = random.choice([-1, 1])
                score = 0
            if event.key == pygame.K_RIGHT and active:
                player_direction = 1
            if event.key == pygame.K_LEFT and active:
                player_direction = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_direction = 0
            if event.key == pygame.K_LEFT:
                player_direction = 0

    if ball_x <= 10 or ball_x >= WIDTH - 10:
        ball_x_direction *= -1

    for i in range(len(squares)):
        # top, bot, left, right, coords
        if ball.colliderect(squares[i][0]) or ball.colliderect(squares[i][1]):
            ball_y_direction *= -1
            board[squares[i][4][0]][squares[i][4][1]] -= 1
            score += 1
        if (ball.colliderect(squares[i][2]) and ball_x_direction == 1) or \
                (ball.colliderect(squares[i][3]) and ball_x_direction == -1):
            ball_x_direction *= -1
            board[squares[i][4][0]][squares[i][4][1]] -= 1
            score += 1

    if ball.colliderect(player):
        if player_direction == ball_x_direction:
            ball_x_speed += 1
        elif player_direction == -ball_x_direction and ball_x_speed > 1:
            ball_x_speed -= 1
        elif player_direction == -ball_x_direction and ball_x_speed == 1:
            ball_x_direction *= -1

        ball_y_direction *= -1

    ball_y += ball_y_direction * ball_y_speed
    ball_x += ball_x_direction * ball_x_speed
    player_x += player_direction * player_speed

    if ball_y <= 10:
        ball_y = 10
        ball_y_direction *= -1

    if ball_y >= HEIGHT - 10 or len(squares) == 0:
        active = False
        player_x = 190
        player_direction = 0
        ball_x = WIDTH / 2
        ball_y = HEIGHT - 30
        ball_x_direction = 0
        ball_y_direction = 0
        ball_x_speed = 5
        ball_y_speed = 5
        create_new = True

    score_text = font.render(f'Score {score}', True, white)
    screen.blit(score_text, (8, 3))
    score_text = font.render(f'Score {score}', True, black)
    screen.blit(score_text, (10, 5))


    if not active:
        start_text = font.render('Space bar to start the game', True, black)
        screen.blit(start_text, (40, 400))

    pygame.display.flip()
pygame.quit()
