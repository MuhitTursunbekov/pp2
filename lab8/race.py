import pygame, sys, random, time

pygame.init()

FramePerSec = pygame.time.Clock()
FramePerSec.tick(60) # Скорость игры

white = (255, 255, 255)

speed, score, cash = 5 , 0 , 0 # Первоначальные настройки игры
height = 600
width = 400
window = (width, height)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("lab8 game")

background = pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab8\Street.png')
coin = pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab8\Coin (3).png')
player = pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab8\Player.png')
enemy = pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab8\Enemy.png') # Загрузка изображений
screen.blit(background, (0, 0))

coin_sound = pygame.mixer.Sound(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab8\coin.mp3')  # Загрузка звука монеты

class Player(pygame.sprite.Sprite): # Определение спрайтов
    def __init__(self):
        super().__init__() 
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)

    def move(self):
        pressed = pygame.key.get_pressed()
        
        if self.rect.left > 5:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-speed, 0)
        if self.rect.right < width - 5:        
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(speed, 0)
        if self.rect.top > 5:
            if pressed[pygame.K_UP]:
                self.rect.move_ip(0, -speed)
        if self.rect.bottom < height - 5:        
            if pressed[pygame.K_DOWN]:
                self.rect.move_ip(0, speed)
            
    def draw(self):
        screen.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, 370), -15)
    
    def move(self):
        self.rect.move_ip(0, 6)
        if self.rect.top > 600:
            self.rect.center = (random.randint(15, 370), -15)

    def respawn(self):
        self.rect.center = (random.randint(30, 370), -15)        

    def draw(self):
        screen.blit(self.image, self.rect)   

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = enemy
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, width - 20), -48)       

    def move(self):
        global score, speed
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            score += 1
            self.rect.center = (random.randint(48, width - 48), -48)

    def draw(self):
        screen.blit(self.image, self.rect)

P = Player()
C = Coin()
E = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E)
coins = pygame.sprite.Group()
coins.add(C)
sprites = pygame.sprite.Group()
sprites.add(P)
sprites.add(E)
sprites.add(C) # Добавление спрайтов в группы

font = pygame.font.SysFont("Times New Roman", 40)

pygame.display.update()
while True:
    screen.blit(background, (0, 0))
    points = font.render('Score: ' + str(score), True, (0 , 0 , 0))
    money = font.render('Cash:  ' + str(cash), True, (0 , 0 , 0))
    screen.blit(points, (10, 10))
    screen.blit(money, (10, 50))
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed_keys[pygame.K_SPACE]:
            pygame.quit()
            sys.exit()

    for sprite in sprites:
        sprite.draw()
        sprite.move()

    if pygame.sprite.spritecollideany(P, coins): # Если игрок касается монеты
        cash += 1
        coin_sound.play()  # Воспроизводим звук монеты
        C.respawn()  # Перемещаем монету в новое место

    if pygame.sprite.spritecollideany(P, enemies): # Если игрок касается врага
        time.sleep(5)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(60)
