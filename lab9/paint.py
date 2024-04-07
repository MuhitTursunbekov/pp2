import pygame
import sys
import random
import time

WIDTH, HEIGHT = 800, 600   # базовый размер окна
FPS = 60
draw = False                # нажатие, зажатие - рисуем, отжали - не рисуем 
lastPos = (0, 0)            # базовая позиция 
radius = 15                 # базовый радиус для инструментов
color = 'blue'              # базовый цвет
mode = 'pen'                # базовый режим

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 100, 10)
GREY = (127, 127, 127)
YELLOW = (255, 255, 0)
PURPLE = (153, 0, 153)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint')
clock = pygame.time.Clock()
screen.fill(pygame.Color('white')) # закрашиваем в белый цвет, чтобы внутри цикла не обновлялось
fontRadius = pygame.font.SysFont('Arial', 66, bold=True)

eraser = pygame.transform.scale(pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\eraser.png'), (40, 40))
cleaner = pygame.transform.scale(pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\clean.png'), (40, 40))
pen = pygame.transform.scale(pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\pen.png'), (40, 40))

eraser_rect = eraser.get_rect(center = (200, 40))
cleaner_rect = cleaner.get_rect(center = (300, 40))
pen_rect = cleaner.get_rect(center = (100, 40))

def drawLine(screen, start, end, width, color):
    pygame.draw.line(screen, pygame.Color(color), start, end, width)

def drawCircle(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    radius = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    pygame.draw.circle(screen, pygame.Color(color), start, int(radius), width)

def drawRectangle(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(screen, pygame.Color(color), rect, width)

def drawSquare(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    side_length = min(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(min(x1, x2), min(y1, y2), side_length, side_length)
    pygame.draw.rect(screen, pygame.Color(color), rect, width)

def drawRightTriangle(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.polygon(screen, pygame.Color(color), [(x1, y1), (x2, y2), (x1, y2)], width)

def drawEquilateralTriangle(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    side_length = min(abs(x2 - x1), abs(y2 - y1))
    height = side_length * (3 ** 0.5) / 2
    pygame.draw.polygon(screen, pygame.Color(color), [(x1, y2), (x2, y2), ((x1 + x2) / 2, y1 - height)], width)

def drawRhombus(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.polygon(screen, pygame.Color(color), [(x1 + (x2 - x1) / 2, y1), (x2, (y1 + y2) / 2), (x1 + (x2 - x1) / 2, y2), (x1, (y1 + y2) / 2)], width)

while True:
    pygame.draw.rect(screen, pygame.Color('white'), (719, 22, 70, 430))

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        # Нажатия на клавиатуру
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rectangle'
            if event.key == pygame.K_c:
                mode = 'circle'
            if event.key == pygame.K_s:
                mode = 'square'
            if event.key == pygame.K_t:
                mode = 'right_tri'
            if event.key == pygame.K_u:
                mode = 'eq_tri'
            if event.key == pygame.K_h:
                mode = 'rhombus'
            if event.key == pygame.K_UP:
                radius = min(200, radius + 1)   # ограничение по максимальному размеру радиуса
            if event.key == pygame.K_DOWN:
                radius = max(1, radius - 1)     # ограничение по минимальному размеру радиуса

        # Нажатие на мышку
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mx, my = pygame.mouse.get_pos()
            draw = True
            if mode == 'pen':
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)
            prevPos = event.pos
            
            if 732 <= mx <= 772 and 25 <= my <= 60:
                mode = 'clean'
            if 732 <= mx <= 772 and 96 <= my <= 136:
                mode = 'pen'
            if 732 <= mx <= 772 and 171 <= my <= 208:
                mode = 'erase'
            if 725 <= mx <= 748 and 242 <= my <= 264:
                color = BLUE
            if 755 <= mx <= 780 and 242 <= my <= 264:
                color = RED
            if 725 <= mx <= 748 and 281 <= my <= 302:
                color = GREEN
            if 755 <= mx <= 780 and 281 <= my <= 302:
                color = BLACK
            if 725 <= mx <= 748 and 321 <= my <= 343:
                color = BROWN
            if 755 <= mx <= 780 and 321 <= my <= 343:
                color = ORANGE
            if 725 <= mx <= 748 and 361 <= my <= 384:
                color = GREY
            if 755 <= mx <= 780 and 361 <= my <= 384:
                color = YELLOW
            if 725 <= mx <= 748 and 401 <= my <= 422:
                color = PURPLE
            if 755 <= mx <= 780 and 401 <= my <= 422:
                color = PINK
            if 731 <= mx <= 780 and 441 <= my <= 488:
                mode = 'rectangle'
            if 731 <= mx <= 780 and 509 <= my <= 567:
                mode = 'circle'

        # Отпускание мышки
        if event.type == pygame.MOUSEBUTTONUP: 
            if mode == 'rectangle':
                drawRectangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'circle':
                drawCircle(screen, prevPos, event.pos, radius, color)
            elif mode == 'square':
                drawSquare(screen, prevPos, event.pos, radius, color)
            elif mode == 'right_tri':
                drawRightTriangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'eq_tri':
                drawEquilateralTriangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'rhombus':
                drawRhombus(screen, prevPos, event.pos, radius, color)
            elif mode == 'clean':
                screen.fill(WHITE)
            draw = False

        # Перемещение мышки
        if event.type == pygame.MOUSEMOTION: 
            if draw and mode == 'pen':
                drawLine(screen, lastPos, event.pos, radius, color)
            elif draw and mode == 'erase':
                drawLine(screen, lastPos, event.pos, radius, 'white')
            lastPos = event.pos

    screen.blit(cleaner, (730, 25)) 
    screen.blit(pen, (730, 100))
    screen.blit(eraser, (730, 175))
    pygame.draw.rect(screen, pygame.Color(BLUE), (725, 240, 25, 25))
    pygame.draw.rect(screen, pygame.Color(RED), (755, 240, 25, 25))
    pygame.draw.rect(screen, pygame.Color(GREEN), (725, 280, 25, 25))
    pygame.draw.rect(screen, pygame.Color(BLACK), (755, 280, 25, 25))
    pygame.draw.rect(screen, pygame.Color(BROWN), (725, 320, 25, 25))
    pygame.draw.rect(screen, pygame.Color(ORANGE), (755, 320, 25, 25))
    pygame.draw.rect(screen, pygame.Color(GREY), (725, 360, 25, 25))
    pygame.draw.rect(screen, pygame.Color(YELLOW), (755, 360, 25, 25))
    pygame.draw.rect(screen, pygame.Color(PURPLE), (725, 400, 25, 25))
    pygame.draw.rect(screen, pygame.Color(PINK), (755, 400, 25, 25))

    # show radius & color
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))
    renderRadius = fontRadius.render(f'{radius}', True, pygame.Color(color))
    screen.blit(renderRadius, (5, 5))

    # display
    pygame.display.flip()
    clock.tick(FPS)
"""
'r': Эта кнопка используется для выбора режима рисования прямоугольника.
'c': Эта кнопка используется для выбора режима рисования круга.
's': Эта кнопка используется для выбора режима рисования квадрата.
't': Эта кнопка используется для выбора режима рисования прямоугольного треугольника.
'u': Эта кнопка используется для выбора режима рисования равностороннего треугольника.
'h': Эта кнопка используется для выбора режима рисования ромба.
"""