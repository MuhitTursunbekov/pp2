import random, sys, pygame, time

# инициализация игры 
pygame.init()

FPS = 60

# размеры экрана
SCREEN_WIDTH = 400 
SCREEN_HEIGHT = 600

# шаги игрока и врага
STEP = 5
ENEMY_STEP = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCORE  = 0 # cчетчик для машин
NUM_OF_COINS = 0 # счетчик для машин 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # установление экрана

pygame.display.set_caption("racer game") # название игры
clock = pygame.time.Clock()

# шрифты и тексты 
score_font = pygame.font.SysFont("Verdana", 20) 
font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, BLACK)

bg = pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\AnimatedStreet.png') # фон игры

# фоновая музыка
pygame.mixer.music.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\background.wav')
pygame.mixer.music.play(-1)

# класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 

    def update(self):
        global SCORE, ENEMY_STEP
        self.rect.move_ip(0, ENEMY_STEP)
        if(self.rect.top > SCREEN_HEIGHT):
            SCORE += 1
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# класс монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\goldcoin.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-1500,-500 ))

    def update(self):
        self.rect.move_ip(0, 5)
        if(self.rect.top > SCREEN_HEIGHT):
            self.top = 0
            self.rect.center = (random.randint(30, 350), random.randint(-1500,-500 ))

    def spawn(self):
        self.rect.center = (random.randint(30, 350), random.randint(-1500,-500 ))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# класс большой монеты
class BIGCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\goldcoin.png')
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(45, SCREEN_WIDTH - 45), random.randint(-1500,-500 ))

    def update(self):
        self.rect.move_ip(0, 5)
        if(self.rect.top > SCREEN_HEIGHT):
            self.top = 0
            self.rect.center = (random.randint(30, 350), random.randint(-1500,-500 ))

    def spawn(self):
        self.rect.center = (random.randint(30, 350), random.randint(-1500,-500 ))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# класс сокровища (большой монеты)
class Treasure(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\treasure.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), random.randint(-1500,-500 ))

    def update(self):
        self.rect.move_ip(0, 5)
        if(self.rect.top > SCREEN_HEIGHT):
            self.top = 0
            self.rect.center = (random.randint(30, 350), random.randint(-1500,-500 ))

    def spawn(self):
        self.rect.center = (random.randint(30, 350), random.randint(-1500,-500 ))

    def draw(self, screenace):
        screenace.blit(self.image, self.rect)

# cоздание cпрайт групп
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = BIGCoin()
T1 = Treasure()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
Bcoins = pygame.sprite.Group()
Bcoins.add(C2)
Treas = pygame.sprite.Group()
Treas.add(T1)

k = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.mixer_music.pause()

            if event.key == pygame.K_w:
                pygame.mixer_music.unpause()

    P1.update()
    E1.update()
    C1.update()
    C2.update()
    T1.update()

    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\coin.mp3').play()
        NUM_OF_COINS += 1
        if NUM_OF_COINS >= k * 50:
            ENEMY_STEP += 1
            k += 1
        C1.spawn() #как только игрок тронул монету, нужно создать новую

    if pygame.sprite.spritecollideany(P1, Bcoins):
        pygame.mixer.Sound(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\coin.mp3').play()
        NUM_OF_COINS += 5
        if NUM_OF_COINS >= k * 50:
            ENEMY_STEP += 1
            k += 1
        C2.spawn()

    if pygame.sprite.spritecollideany(P1, Treas):
        pygame.mixer.Sound(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\coin.mp3').play()
        NUM_OF_COINS += 10
        if NUM_OF_COINS >= k * 50:
            ENEMY_STEP += 1
            k += 1
        T1.spawn() 

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab9\crash.wav').play()
        time.sleep(1)
                   
        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
          
        time.sleep(2)
        pygame.quit()
        sys.exit()    

    screen.blit(bg, (0, 0))
    score_img = score_font.render('Number of passing cars: '+ str(SCORE), True, BLACK)
    coin_score_img = score_font.render('Number of collected coins: '+ str(NUM_OF_COINS), True, BLACK)
    speed_img = score_font.render('Enemy speed: '+ str(ENEMY_STEP), True, BLACK)

    screen.blit(score_img, (10, 10)) # позиция счетчика машин
    screen.blit(coin_score_img, (10, 30)) # позиция счетчика монет
    screen.blit(speed_img, (10, 50))

    E1.draw(screen)
    P1.draw(screen)
    C1.draw(screen)
    C2.draw(screen)
    T1.draw(screen)
    pygame.display.update()
    clock.tick(FPS)