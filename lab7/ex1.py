import pygame
import datetime
r'...'
pygame.init()

# Установка размера окна
size = w, h = (1400, 1050)

# Получение текущего времени
time = datetime.datetime.now()

# Создание окна приложения
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Часы с Микки-Маусом')

# Загрузка изображения Микки-Мауса
mickey = pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab7\mainclock.png')

# Загрузка изображений стрелок (секундной и минутной)
seconds = pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab7\leftarm.png')
minutes = pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab7\rightarm.png')

# Установка начального угла поворота для стрелок
angle_seconds = -(int(time.strftime("%S")) * 6) - 6
angle_minutes = -(int(time.strftime("%M")) * 6 + (int(time.strftime("%S")) * 6 / 60)) - 54

# Функция для поворота изображения
def rotate(image, angle):
    return pygame.transform.rotate(image, angle)

# Основной цикл приложения
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение текущего времени
    time = datetime.datetime.now()

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Отрисовка Микки-Мауса на фоне
    screen.blit(mickey, (0, 0))

    # Поворот и отрисовка стрелок (секундной и минутной)
    rotated_seconds = rotate(seconds, angle_seconds)
    rotated_minutes = rotate(minutes, angle_minutes)
    screen.blit(rotated_seconds, (w//2 - rotated_seconds.get_width()//2, h//2 - rotated_seconds.get_height()//2))
    screen.blit(rotated_minutes, (w//2 - rotated_minutes.get_width()//2, h//2 - rotated_minutes.get_height()//2))

    # Обновление углов поворота для стрелок
    angle_seconds -= 6
    angle_minutes -= 6 / 60

    # Обновление экрана
    pygame.display.flip()

    # Установка частоты кадров в секунду
    clock.tick(60)

pygame.quit()
