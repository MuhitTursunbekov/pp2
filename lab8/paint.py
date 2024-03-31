import pygame
import math

# Инициализация pygame
pygame.init()

# Установка размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Настройки кисти
brush_color = BLACK
brush_size = 5
eraser_size = 20
mode = "pen"  # Режим по умолчанию - карандаш

# Функция для рисования плавной линии
def draw_smooth_line(surface, color, start, end, radius):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(surface, color, (x, y), radius)

# Основной цикл программы
running = True
drawing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                drawing = True
                start_pos = event.pos
            elif event.button == 4:  # Колесико вверх
                if mode == "pen":
                    brush_size = min(50, brush_size + 2)
                elif mode == "eraser":
                    eraser_size = min(50, eraser_size + 2)
            elif event.button == 5:  # Колесико вниз
                if mode == "pen":
                    brush_size = max(1, brush_size - 2)
                elif mode == "eraser":
                    eraser_size = max(1, eraser_size - 2)
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode == "rectangle":
                pygame.draw.rect(screen, brush_color, (start_pos[0], start_pos[1], event.pos[0] - start_pos[0], event.pos[1] - start_pos[1]), brush_size)
            elif mode == "circle":
                radius = math.hypot(event.pos[0] - start_pos[0], event.pos[1] - start_pos[1])
                pygame.draw.circle(screen, brush_color, start_pos, int(radius), brush_size)
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                end_pos = event.pos
                if mode == "pen":
                    pygame.draw.line(screen, brush_color, start_pos, end_pos, brush_size * 2)
                    draw_smooth_line(screen, brush_color, start_pos, end_pos, brush_size)
                    start_pos = end_pos
                elif mode == "eraser":
                    pygame.draw.circle(screen, WHITE, end_pos, eraser_size)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Режим карандаша
                mode = "pen"
            elif event.key == pygame.K_r:  # Режим прямоугольника
                mode = "rectangle"
            elif event.key == pygame.K_c:  # Режим окружности
                mode = "circle"
            elif event.key == pygame.K_e:  # Режим ластика
                mode = "eraser"
            elif event.key == pygame.K_ESCAPE:  # Очистить экран
                screen.fill(WHITE)
            elif event.key == pygame.K_b:  # Черный цвет
                brush_color = BLACK
            elif event.key == pygame.K_w:  # Белый цвет
                brush_color = WHITE
            elif event.key == pygame.K_g:  # Зеленый цвет
                brush_color = GREEN
            elif event.key == pygame.K_y:  # Желтый цвет
                brush_color = YELLOW
            elif event.key == pygame.K_o:  # Оранжевый цвет
                brush_color = ORANGE

    # Рисование фигур в зависимости от выбранного режима
    if mode == "rectangle":
        if drawing:
            pygame.draw.rect(screen, brush_color, (start_pos[0], start_pos[1], pygame.mouse.get_pos()[0] - start_pos[0], pygame.mouse.get_pos()[1] - start_pos[1]), brush_size)

    pygame.display.flip()

# Выход из программы
pygame.quit()
