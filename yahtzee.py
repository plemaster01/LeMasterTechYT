import random
import pygame

pygame.init()

WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Yahtzee!')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 18)
roll = False
numbers = [7, 8, 9, 10, 11]
selected = [False, False, False, False, False]
clicked = False
draw_clicked = 30
count = 110
rolls_left = 3
scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
choice = [False, False, False, False, False, False, False, False, False, False, False, False, False]
done = [False, False, False, False, False, False, False, False, False, False, False, False, False]
possible = [False, False, False, False, False, False, False, False, False, False, False, False, False]
totals = [0, 0, 0, 0, 0, 0, 0]
something_selected = False
bonus_time = False
game_over = False
high_score = 0
score = 0
restart = ''


class Choice:
    def __init__(self, x_pos, y_pos, text, select, possibles, dones, my_score):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.selected = select
        self.possible = possibles
        self.done = dones
        self.score = my_score

    def draw(self):
        pygame.draw.line(screen, (0, 0, 0), (self.x_pos, self.y_pos + 31), (self.x_pos + 225, self.y_pos + 31), 2)
        name_text = ''
        if not self.done:
            if self.possible:
                name_text = font.render(self.text, True, (34, 140, 34))
            elif not self.possible:
                name_text = font.render(self.text, True, (255, 0, 0))
        else:
            name_text = font.render(self.text, True, (0, 0, 0))
        if self.selected:
            pygame.draw.rect(screen, (20, 35, 30), [self.x_pos, self.y_pos + 2, 155, 30])
        screen.blit(name_text, (self.x_pos + 5, self.y_pos + 10))
        score_text = font.render(str(self.score), True, (0, 0, 255))
        screen.blit(score_text, (self.x_pos + 165, self.y_pos + 10))


class Dice:
    def __init__(self, x_pos, y_pos, num, key):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = num
        global selected
        self.key = key
        self.active = selected[self.key]
        self.die = ''

    def draw(self):
        self.die = pygame.draw.rect(screen, (255, 255, 255), [self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.number == 1:
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 50, self.y_pos + 50), 10)
        if self.number == 2:
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 3:
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 4:
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 80, self.y_pos + 20), 10)
        if self.number == 5:
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 80, self.y_pos + 20), 10)
        if self.number == 6:
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 20, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 80, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 80, self.y_pos + 20), 10)
        if self.active:
            pygame.draw.rect(screen, (255, 0, 0), [self.x_pos, self.y_pos, 100, 100], 4, 5)

    def check_click(self, coordinates):
        if self.die.collidepoint(coordinates):
            if selected[self.key]:
                selected[self.key] = False
            elif not selected[self.key]:
                selected[self.key] = True


def restart_function():
    global roll
    global numbers
    global selected
    global clicked
    global rolls_left
    global scores
    global choice
    global done
    global possible
    global totals
    global something_selected
    global score
    roll = False
    numbers = [7, 8, 9, 10, 11]
    selected = [False, False, False, False, False]
    clicked = False
    rolls_left = 3
    scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    choice = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    done = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    possible = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    totals = [0, 0, 0, 0, 0, 0, 0]
    something_selected = False
    score = 0



def make_choice(num, my_list, done_list):
    for index in range(len(my_list)):
        my_list[index] = False
    if not done_list[num]:
        my_list[num] = True
    return my_list


def draw_stuff():
    global game_over
    global game_score
    roll_text = font.render('Roll', True, (255, 255, 255))
    screen.blit(roll_text, (130, 165))
    accept_text = font.render('Accept Turn', True, (255, 255, 255))
    screen.blit(accept_text, (390, 165))
    turns_text = font.render('Rolls Left This Turn: ' + str(rolls_left), True, (255, 255, 255))
    screen.blit(turns_text, (15, 15))
    but_text = font.render('Click a Die to Keep It Or Release It', True, (255, 255, 255))
    screen.blit(but_text, (280, 15))
    pygame.draw.rect(screen, (255, 255, 255), [0, 200, 225, HEIGHT - 200])
    pygame.draw.line(screen, (0, 0, 0), (0, 40), (WIDTH, 40), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (WIDTH, 200), 3)
    pygame.draw.line(screen, (0, 0, 0), (600, 0), (600, 200), 3)
    pygame.draw.line(screen, (0, 0, 0), (250, 0), (250, 40), 3)
    pygame.draw.line(screen, (0, 0, 0), (155, 200), (155, HEIGHT), 3)
    pygame.draw.line(screen, (0, 0, 0), (225, 200), (225, HEIGHT), 3)
    if game_over:
        over_text = font.render('Game Over! Restart to Play Again', True, (255, 255, 255))
        screen.blit(over_text, (280, 280))
    score_text = font.render('Score: ' + str(game_score), True, (255, 255, 255))
    screen.blit(score_text, (280, 340))
    high_score_text = font.render('High Score: ' + str(high_score), True, (255, 255, 255))
    screen.blit(high_score_text, (280, 370))


def draw_dice():
    die1.draw()
    die2.draw()
    die3.draw()
    die4.draw()
    die5.draw()


def draw_options():
    ones.draw()
    twos.draw()
    threes.draw()
    fours.draw()
    fives.draw()
    sixes.draw()
    three_kind.draw()
    four_kind.draw()
    full_house.draw()
    small_straight.draw()
    large_straight.draw()
    yahtzee.draw()
    chance.draw()
    lower_total1.draw()
    lower_bonus.draw()
    lower_total2.draw()
    lower_total.draw()
    upper_total.draw()
    grand_total.draw()
    bonus.draw()


def check_possibilities(pos_list, nums):
    pos_list[0] = True
    pos_list[1] = True
    pos_list[2] = True
    pos_list[3] = True
    pos_list[4] = True
    pos_list[5] = True
    pos_list[12] = True
    max_count = 0

    for index in range(1, 7):
        if nums.count(index + 1) > max_count:
            max_count = nums.count(index + 1)
    if max_count >= 3:
        pos_list[6] = True
        if max_count >= 4:
            pos_list[7] = True
            if max_count >= 5:
                pos_list[11] = True
    if max_count < 3:
        pos_list[6] = False
        pos_list[7] = False
        pos_list[8] = False
        pos_list[11] = False
    elif max_count == 3:
        pos_list[7] = False
        pos_list[11] = False
        checker = False
        for index in range(len(nums)):
            if nums.count(nums[index]) == 2:
                pos_list[8] = True
                checker = True
        if not checker:
            pos_list[8] = False
    elif max_count == 4:
        pos_list[11] = False

    lowest = 10
    highest = 0
    for index in range(len(nums)):
        if nums[index] < lowest:
            lowest = nums[index]
        if nums[index] > highest:
            highest = nums[index]

    if lowest + 1 in nums and lowest + 2 in nums and lowest + 3 in nums and lowest + 4 in nums:
        pos_list[10] = True
    else:
        pos_list[10] = False
    if (lowest + 1 in nums and lowest + 2 in nums and lowest + 3 in nums) or (
            highest - 1 in nums and highest - 2 in nums and highest - 3 in nums):
        pos_list[9] = True
    else:
        pos_list[9] = False
    return pos_list


def check_scores(select_list, number_list, possible_list, points):
    active = 0
    for index in range(len(select_list)):
        if select_list[index]:
            active = index
    if active == 0:
        points = number_list.count(1)
    elif active == 1:
        points = number_list.count(2) * 2
    elif active == 2:
        points = number_list.count(3) * 3
    elif active == 3:
        points = number_list.count(4) * 4
    elif active == 4:
        points = number_list.count(5) * 5
    elif active == 5:
        points = number_list.count(6) * 6
    elif active == 6 or active == 7:
        if possible_list[active]:
            points = sum(number_list)
        else:
            points = 0
    elif active == 8:
        if possible_list[active]:
            points = 25
        else:
            points = 0
    elif active == 9:
        if possible_list[active]:
            points = 30
        else:
            points = 0
    elif active == 10:
        if possible_list[active]:
            points = 40
        else:
            points = 0
    elif active == 11:
        if possible_list[active]:
            points = 50
        else:
            points = 0
    elif active == 12:
        points = sum(number_list)
    return points


def check_totals(totals_list, scores_list, my_bonus):
    totals_list[0] = scores_list[0] + scores_list[1] + scores_list[2] + scores_list[3] + scores_list[4] + scores_list[5]
    if totals_list[0] >= 63:
        totals_list[1] = 35
    else:
        totals_list[1] = 0
    totals_list[2] = totals_list[0] + totals_list[1]

    totals_list[4] = scores_list[6] + scores_list[7] + scores_list[8] + scores_list[9] + scores_list[10] + \
        scores_list[11] + scores_list[12]
    totals_list[5] = totals_list[2]
    totals_list[6] = totals_list[4] + totals_list[5]
    if my_bonus:
        totals_list[3] += 100
        my_bonus = False
    return totals_list, my_bonus


running = True
while running:
    timer.tick(fps)
    screen.fill((128, 128, 128))
    button1 = pygame.draw.rect(screen, (0, 0, 0), [10, 160, 280, 30])
    button2 = pygame.draw.rect(screen, (0, 0, 0), [310, 160, 280, 30])
    if game_over:
        restart = pygame.draw.rect(screen, (0, 0, 0), [277, 272, 300, 30])
    die1 = Dice(10, 50, numbers[0], 0)
    die2 = Dice(130, 50, numbers[1], 1)
    die3 = Dice(250, 50, numbers[2], 2)
    die4 = Dice(370, 50, numbers[3], 3)
    die5 = Dice(490, 50, numbers[4], 4)
    ones = Choice(0, 200, '1s', choice[0], possible[0], done[0], scores[0])
    twos = Choice(0, 230, '2s', choice[1], possible[1], done[1], scores[1])
    threes = Choice(0, 260, '3s', choice[2], possible[2], done[2], scores[2])
    fours = Choice(0, 290, '4s', choice[3], possible[3], done[3], scores[3])
    fives = Choice(0, 320, '5s', choice[4], possible[4], done[4], scores[4])
    sixes = Choice(0, 350, '6s', choice[5], possible[5], done[5], scores[5])
    lower_total1 = Choice(0, 380, 'Upper Score', False, False, True, totals[0])
    lower_bonus = Choice(0, 410, 'Bonus if >= 63', False, False, True, totals[1])
    lower_total2 = Choice(0, 440, 'Upper Total', False, False, True, totals[2])
    three_kind = Choice(0, 470, '3 of Kind', choice[6], possible[6], done[6], scores[6])
    four_kind = Choice(0, 500, '4 of Kind', choice[7], possible[7], done[7], scores[7])
    full_house = Choice(00, 530, 'Full House', choice[8], possible[8], done[8], scores[8])
    small_straight = Choice(0, 560, 'Sm. Straight', choice[9], possible[9], done[9], scores[9])
    large_straight = Choice(0, 590, 'Lg. Straight', choice[10], possible[10], done[10], scores[10])
    yahtzee = Choice(0, 620, 'YAHTZEE', choice[11], possible[11], done[11], scores[11])
    chance = Choice(0, 650, 'Chance', choice[12], possible[12], done[12], scores[12])
    bonus = Choice(0, 680, 'YAHTZEE Bonus', False, False, True, totals[3])
    lower_total = Choice(0, 710, 'Lower Total', False, False, True, totals[4])
    upper_total = Choice(0, 740, 'Upper Total', False, False, True, totals[5])
    grand_total = Choice(0, 770, 'Grand Total', False, False, True, totals[6])
    game_score = totals[6]
    draw_stuff()
    draw_dice()
    draw_options()
    possible = check_possibilities(possible, numbers)
    score = check_scores(choice, numbers, possible, score)
    totals, bonus_time = check_totals(totals, scores, bonus_time)

    if draw_clicked < 30:
        outline_button = pygame.draw.rect(screen, (70, 70, 70), [10, 160, 280, 30], 4)
        draw_clicked += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over and restart.collidepoint(event.pos):
                restart_function()
                game_over = False
            die1.check_click(event.pos)
            die2.check_click(event.pos)
            die3.check_click(event.pos)
            die4.check_click(event.pos)
            die5.check_click(event.pos)
            if button1.collidepoint(event.pos) and rolls_left > 0:
                roll = True
                rolls_left -= 1
                draw_clicked = 0
            if button2.collidepoint(event.pos) and something_selected and rolls_left < 3:
                if scores[11] == 50 and done[11] and possible[11]:
                    bonus_time = True
                for i in range(len(choice)):
                    if choice[i]:
                        done[i] = True
                        scores[i] = score
                        choice[i] = False
                for i in range(len(selected)):
                    selected[i] = False
                rolls_left = 3
                numbers = [7, 8, 9, 10, 11]
                something_selected = False
            if 0 <= event.pos[0] <= 155:
                if 200 < event.pos[1] < 381 or 470 < event.pos[1] < 681:
                    if 200 < event.pos[1] < 230:
                        clicked = 0
                    elif 230 < event.pos[1] < 260:
                        clicked = 1
                    elif 260 < event.pos[1] < 290:
                        clicked = 2
                    elif 290 < event.pos[1] < 320:
                        clicked = 3
                    elif 320 < event.pos[1] < 350:
                        clicked = 4
                    elif 350 < event.pos[1] < 380:
                        clicked = 5
                    elif 470 < event.pos[1] < 500:
                        clicked = 6
                    elif 500 < event.pos[1] < 530:
                        clicked = 7
                    elif 530 < event.pos[1] < 560:
                        clicked = 8
                    elif 560 < event.pos[1] < 590:
                        clicked = 9
                    elif 590 < event.pos[1] < 620:
                        clicked = 10
                    elif 620 < event.pos[1] < 650:
                        clicked = 11
                    elif 650 < event.pos[1] < 680:
                        clicked = 12
                    choice = make_choice(clicked, choice, done)

    if roll:
        for number in range(len(numbers)):
            if not selected[number]:
                numbers[number] = random.randint(1, 6)
        roll = False

    for i in range(len(possible)):
        if choice[i] and not possible[i]:
            click_text = font.render('Choosing that option will give you a zero!', True, (155, 34, 34))
            screen.blit(click_text, (230, 205))
        if choice[i]:
            something_selected = True

    if game_over:
        if game_score > high_score:
            high_score = game_score

    if False not in done:
        game_over = True

    pygame.display.flip()
pygame.quit()
