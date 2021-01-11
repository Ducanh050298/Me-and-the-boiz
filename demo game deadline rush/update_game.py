import pygame
import math

# Initialize the game
pygame.init()

# Create screen
screen = pygame.display.set_mode((1200, 800))

# Background
background1 = pygame.image.load('wjbu_1.png')
background1_X = 0
background1_X_change = 0

background2 = pygame.image.load('wjbu_2.png')
background2_X = 1200
background2_X_change = 0

background3 = pygame.image.load('rmit.png')

background4 = pygame.image.load('fail.png')

# Title and icon
pygame.display.set_caption("Deadline Rush")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

# Monster
monsterIMG = pygame.image.load('monster.png')
monsterX, monsterY = 100, 600
monsterX_change = 0

# Runner
runnerIMG = pygame.image.load('runner.png')
runnerX, runnerY = 400, 600
runnerX_change = 0

# Object_1
object_1_IMG = pygame.image.load('object_1.png')
object_1_X, object_1_Y = 1000, 600
object_1_X_change = 0

# Object_1
object_2_IMG = pygame.image.load('object_1.png')
object_2_X, object_2_Y = 1800, 600
object_2_X_change = 0

# Question
question = pygame.font.Font('freesansbold.ttf', 32)
question_surface = question.render('Which will return True?', True, (235, 64, 52))

# Answer
answer_1 = pygame.font.Font('freesansbold.ttf', 32)
answer_surface_1 = answer_1.render('A. 5==5', False, (52, 55, 235))

answer_2 = pygame.font.Font('freesansbold.ttf', 32)
answer_surface_2 = answer_2.render('B. 5=5', False, (52, 55, 235))

# Game over
game_over = pygame.font.Font('freesansbold.ttf', 64)
game_over_surface = game_over.render('GAME OVER', False, (235, 64, 52))

# Pause
pauseIMG = pygame.image.load('pause.png')
pause_backgroundIMG = pygame.image.load('pause_background.png')

# Move on
move_on = pygame.font.Font('freesansbold.ttf', 64)
move_on_surface = move_on.render('CORRECT!, please move on', False, (3, 252, 36))

# Advise
advice = pygame.font.Font('freesansbold.ttf', 32)
advice_surface = advice.render('You should review more on boolean type', False, (3, 252, 36))

# Here
here = pygame.font.Font('freesansbold.ttf', 32)
here_surface = here.render('Here is the link', False, (3, 252, 36))

# Link
link = pygame.font.Font('freesansbold.ttf', 32)
link = link.render('https://www.w3schools.com/python/python_booleans.asp', False, (235, 64, 52))

# Pause continue
pause_text = pygame.font.Font('freesansbold.ttf', 32)
pause_text_surface = pause_text.render('Click here to continue', False, (3, 252, 36))


def monster(x, y):
    screen.blit(monsterIMG, (x, y))


def runner(x, y):
    screen.blit(runnerIMG, (x, y))


def object_1(x, y):
    screen.blit(object_1_IMG, (x, y))


def distance():
    return math.sqrt((object_1_X - runnerX) ** 2 + (object_1_Y - runnerY) ** 2)


def pop_question():
    pygame.draw.rect(screen, (255, 255, 255), (800, 200, 400, 400))
    screen.blit(question_surface, (800, 200))
    screen.blit(answer_surface_1, (800, 300))
    screen.blit(answer_surface_2, (800, 400))


# Game loop
running = True
location = (0, 0)
while running:
    for event in pygame.event.get():
        # Quit function
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            location = pygame.mouse.get_pos()
            print(location)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                object_1_X_change = -5
                object_2_X_change = -5
                background1_X_change = -5
                background2_X_change = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                object_1_X_change = 0
                object_2_X_change = 0
                background1_X_change = 0
                background2_X_change = 0
            if event.key == pygame.K_b:
                screen.fill((0, 0, 0))

    object_1_X += object_1_X_change
    object_2_X += object_2_X_change

    background1_X += background1_X_change
    background2_X += background2_X_change

    if object_1_X <= 0:
        location = (0, 0)
        object_1_X = 1000
    if background1_X <= -1200:
        background1_X = 1200

    if background2_X <= -1200:
        background2_X = 1200

    screen.blit(background1, (background1_X, 0))
    screen.blit(background2, (background2_X, 0))

    monster(monsterX, monsterY)
    runner(runnerX, runnerY)
    object_1(object_1_X, object_1_Y)
    screen.blit(pauseIMG, (1000, 100))

    if 1000 <= location[0] <= 1064 and 100 <= location[1] <= 164:
        screen.blit(pause_backgroundIMG, (0, 0))
        screen.blit(pause_text_surface, (400, 200))

    if distance() < 50:
        pop_question()
        if not 190 <= location[1] <= 330 and 750 <= location[0] <= 830:
            screen.blit(background3, (0, 0))
            screen.blit(game_over_surface, (200, 100))
            screen.blit(advice_surface, (230, 200))
            screen.blit(here_surface, (230, 300))
            screen.blit(link, (230, 400))
        elif 190 <= location[1] <= 330 and 750 <= location[0] <= 830:
            screen.blit(move_on_surface, (100, 100))

    pygame.display.update()
