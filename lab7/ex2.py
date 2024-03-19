import pygame
import os

# Определяем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)

pygame.init()
pygame.mixer.init()

# Инициализация шрифтов
font = pygame.font.Font(None, 36)

# Определение размеров экрана
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))

# Получение текущей директории скрипта
current_directory = os.path.dirname(__file__)

# Относительные пути к аудиофайлам
songs = [
    os.path.join(current_directory, r'C:\Users\User\OneDrive\Рабочий стол\pp2\Adele – Rolling in the Deep.mp3'),
    os.path.join(current_directory, r'C:\Users\User\OneDrive\Рабочий стол\pp2\Adele – Skyfall.mp3'),
    os.path.join(current_directory, r'C:\Users\User\OneDrive\Рабочий стол\pp2\tears for fears-everybody wants to rule the world.mp3')
]

# Переменные для управления музыкой
current_song_index = 0
currently_playing_song = None
paused = False

def play_song(index):
    global currently_playing_song
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()
    currently_playing_song = index

def stop_song():
    pygame.mixer.music.stop()

def pause_resume_song():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_song(current_song_index)

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_song(current_song_index)

# Запуск проигрывателя
play_song(current_song_index)

# Главный цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause_resume_song()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                previous_song()
            elif event.key == pygame.K_DOWN:
                stop_song()

    # Отрисовка интерфейса
    window.fill(WHITE)

    # Отображение текущей песни
    current_song_text = font.render("Now Playing: " + os.path.basename(songs[currently_playing_song]), True, BLACK)
    window.blit(current_song_text, (20, 20))

    # Отображение кнопок управления
    play_pause_text = font.render("SPACE - Play/Pause", True, BLACK)
    next_text = font.render("RIGHT ARROW - Next", True, BLACK)
    previous_text = font.render("LEFT ARROW - Previous", True, BLACK)
    stop_text = font.render("DOWN ARROW - Stop", True, BLACK)

    window.blit(play_pause_text, (20, 100))
    window.blit(next_text, (20, 150))
    window.blit(previous_text, (20, 200))
    window.blit(stop_text, (20, 250))

    pygame.display.flip()

pygame.quit()
