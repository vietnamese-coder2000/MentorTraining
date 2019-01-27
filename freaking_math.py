import pygame, sys, random
from pygame.locals import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BRIGHT_BLUE = (0, 50, 255)
DARK_TURQUOISE = (0, 204, 0)
GRAY = (100, 100, 100)
NAVY_BLUE = (60, 60, 100)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BOX_O_LEFT, BOX_O_TOP = 30, 500
BOX_X_LEFT, BOX_X_TOP = 280, 500
BOX_WIDTH = 200
BOX_HEIGHT = 200
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800
background_colors = [BLACK, BLUE, GREEN, RED, BRIGHT_BLUE, DARK_TURQUOISE, PURPLE, CYAN, ORANGE, YELLOW, GRAY, NAVY_BLUE]
text_color = WHITE


def main():
    global DISPLAY_SURFACE
    pygame.init()
    DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    mousex = 0
    mousey = 0
    pygame.display.set_caption('Freaking Math')
    BACKGROUND_COLOR = background_colors[random.randint(0, len(background_colors) - 1)]
    first_number = random.randint(0, 200)
    second_number = random.randint(0, 200)
    operators = ['+', '-']
    operator = operators[random.randint(0, 1)]
    real_answer = first_number + second_number if operator == '+' else (first_number - second_number)
    answers = [True, False]
    answer = answers[random.randint(0, 1)]
    difference = random.randint(-20, 20)
    while difference == 0:
        difference = random.randint(-20 , 20)
    while True:
        mouseClicked = False
        DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
        if answer:
            display_equation(DISPLAY_SURFACE, first_number, second_number, operator, real_answer, BACKGROUND_COLOR, WHITE)
        else:
            display_equation(DISPLAY_SURFACE, first_number, second_number, operator, real_answer + difference, BACKGROUND_COLOR, WHITE)
        draw_x_box(DISPLAY_SURFACE, BOX_X_LEFT, BOX_X_TOP, BOX_WIDTH, BOX_HEIGHT)
        draw_o_box(DISPLAY_SURFACE, BOX_O_LEFT, BOX_O_TOP, BOX_WIDTH, BOX_HEIGHT)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos

            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        answer_box = get_box_at_pixel(mousex, mousey)

        if mouseClicked:
            if answer_box == "X":
                if not answer:
                    answers = [True, False]
                    answer = answers[random.randint(0, 1)]
                    BACKGROUND_COLOR = background_colors[random.randint(0, len(background_colors) - 1)]
                    first_number = random.randint(0, 200)
                    second_number = random.randint(0, 200)
                    operators = ['+', '-']
                    operator = operators[random.randint(0, 1)]
                    real_answer = first_number + second_number if operator == '+' else (first_number - second_number)
                    difference = random.randint(-20, 20)
                    while difference == 0:
                        difference = random.randint(-20 , 20)
                else:

                    BACKGROUND_COLOR = background_colors[random.randint(0, len(background_colors) - 1)]
                    for i in range(1000):
                        DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
                        end_game(DISPLAY_SURFACE, WHITE, BACKGROUND_COLOR)
                        pygame.display.update()
                    break
            elif answer_box == "O":
                if not answer:

                    BACKGROUND_COLOR = background_colors[random.randint(0, len(background_colors) - 1)]
                    for i in range(1000):
                        DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
                        end_game(DISPLAY_SURFACE, WHITE, BACKGROUND_COLOR)
                        pygame.display.update()
                    break
                else:
                    answers = [True, False]
                    answer = answers[random.randint(0, 1)]
                    BACKGROUND_COLOR = background_colors[random.randint(0, len(background_colors) - 1)]
                    first_number = random.randint(0, 200)
                    second_number = random.randint(0, 200)
                    operators = ['+', '-']
                    operator = operators[random.randint(0, 1)]
                    real_answer = first_number + second_number if operator == '+' else (first_number - second_number)
                    difference = random.randint(-20, 20)
                    while difference == 0:
                        difference = random.randint(-20, 20)
        pygame.display.update()


def draw_x_box(surface, x, y, width, height):
    pygame.draw.rect(surface, WHITE, (x, y, width, height))
    pygame.draw.line(surface, RED, (x + 10, y + 10), (x + width - 10, y + height - 10), 10)
    pygame.draw.line(surface, RED, (x + 10, y + height - 10), (x + width - 10, y + 10), 10)


def draw_o_box(surface, x, y, width, height):
    pygame.draw.rect(surface, WHITE, (x, y, width, height))
    pygame.draw.circle(surface, BLUE, (x + width // 2, y + height // 2), width // 2 - 10, 5)


def get_box_at_pixel(x, y):
    left, top = BOX_X_LEFT, BOX_X_TOP
    boxRect = pygame.Rect(left, top, BOX_WIDTH, BOX_HEIGHT)
    if boxRect.collidepoint(x, y):
        return "X"
    left, top = BOX_O_LEFT, BOX_O_TOP
    boxRect = pygame.Rect(left, top, BOX_WIDTH, BOX_HEIGHT)
    if boxRect.collidepoint(x, y):
        return "O"
    return None

def display_equation(surface, first_number, second_number, operator, answer, background_color, text_color):
    fontObj = pygame.font.Font('freesansbold.ttf', 60)
    textSurfaceObj = fontObj.render(str(first_number) + ' ' + operator + ' ' + str(second_number) + ' = '
                                    + str(answer), True, text_color, background_color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (250, 150)
    surface.blit(textSurfaceObj, textRectObj)

def end_game(surface, text_color, background_color):
    fontObj = pygame.font.Font('freesansbold.ttf', 60)
    textSurfaceObj = fontObj.render("Congratulation!", True, text_color, background_color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (250, 300)
    surface.blit(textSurfaceObj, textRectObj)

    fontObj2 = pygame.font.Font('freesansbold.ttf', 40)
    textSurfaceObj2 = fontObj2.render("You're officially a loser!", True, text_color, background_color)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (250, 390)
    surface.blit(textSurfaceObj2, textRectObj2)

main()