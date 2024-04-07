import pygame, random, time

green = (0, 100, 0)
black = (0, 0, 0)
red = (255, 0, 0)
grey = (69, 69, 69)
yellow = (250, 253, 15)
blue = (0, 0, 255)

pygame.init()

WIDTH, HEIGHT = 500, 500 # Размеры экрана

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # создание экрана

class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]  
        self.dx = 5 
        self.dy = 0
        self.add_size = False
        self.add_sizeBIG=False
        self.add_sizeTime=False
        self.radius = 8
        self.speed = 25
        self.score = 0
        self.level = 1
        self.running = True
        self.font= pygame.font.SysFont("comicsansms", 20)

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, black, element, self.radius)

    def add_to_snake(self):
        if self.add_sizeBIG == True:
            self.size += 3
            self.elements.append([0,0])
            self.elements.append([0,0])
            self.elements.append([0,0])
            self.add_sizeBIG = False

        elif self.add_sizeTime == True:
            self.size += 5
            self.elements.append([0,0])
            self.elements.append([0,0])
            self.elements.append([0,0])
            self.elements.append([0,0])
            self.elements.append([0,0])
            self.add_sizeTime = False

        else:
            self.size += 1
            self.elements.append([0, 0])
        self.add_size = False

    def message1(self):
        text1 = self.font.render("Current level: " + str(self.level), True,black)
        return text1

    def message2(self):
        text2 = self.font.render("Current score: " + str(self.score), True,black)
        return text2

    def message3(self):
        text3 = self.font.render("Current speed: "+ str(self.speed), True, black)
        return text3

    def move(self):
        if self.add_size:
            self.add_to_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
        if self.elements[0][0] > WIDTH: 
            self.elements[0][0] = 0 
        elif self.elements[0][0] < 0: 
            self.elements[0][0] = WIDTH
        if self.elements[0][1] > HEIGHT: 
            self.elements[0][1] = 0
        elif self.elements[0][1] < 0: 
            self.elements[0][1] = HEIGHT

    def collision_check(self):
        for pos in self.elements[1:]:
            if self.elements[0][0] == pos[0] and self.elements[0][1] == pos[1]:
                time.sleep(1.5)
                return True
        return False

    def eat(self, foodx1, foody1): #for regular red food
        if foodx1 <= self.elements[0][0] <= foodx1 + 13 and foody1 <= self.elements[0][1] <= foody1 + 13:
            self.score+=1
            if self.score % 10 == 0:
                self.speed += 5
                self.level+=1
            return True
        return False 

    def eatBIG(self,bfoodx,bfoody): #for yellow food which just as red but weights 3 points
        if bfoodx <= self.elements[0][0] <= bfoodx + 13 and bfoody <= self.elements[0][1] <= bfoody + 13:
            self.score+=3
            if self.score % 10 == 0:
                self.speed += 5
                self.level+=1
            return True
        return False
        
    def eatTime(self,tfoodx,tfoody): #for blue food that dissapears every 5 seconds
        if tfoodx <= self.elements[0][0] <= tfoodx + 13 and tfoody <= self.elements[0][1] <= tfoody + 13:
            self.score+=5 #it weights 5 points
            if self.score % 10 == 0:
                self.speed += 5
                self.level+=1
            return True
        return False

class Food:
    def __init__(self):
        self.x, self.y  = random.randint(0, WIDTH // 10) * 10, random.randint(0, HEIGHT // 10) * 10

    def gen(self):
        self.x, self.y  = random.randint(0, WIDTH // 10) * 10, random.randint(0, HEIGHT // 10) * 10

    def draw(self):
        pygame.draw.rect(screen, red, (self.x, self.y, 13, 13))
        
class BFood:
    def __init__(self):
        self.x, self.y  = random.randint(0, WIDTH // 10) * 10, random.randint(0, HEIGHT // 10) * 10

    def gen(self):
        self.x, self.y  = random.randint(0, WIDTH // 10) * 10, random.randint(0, HEIGHT // 10) * 10

    def draw(self):
        pygame.draw.rect(screen, yellow, (self.x, self.y, 13, 13))

class TFood:
    def __init__(self):
        self.x, self.y  = random.randint(0, WIDTH // 10) * 10, random.randint(0, HEIGHT // 10) * 10

    def gen(self):
        self.x, self.y  = random.randint(0, WIDTH // 10) * 10, random.randint(0, HEIGHT // 10) * 10

    def draw(self):
        pygame.draw.rect(screen, blue, (self.x, self.y, 13, 13))

snake = Snake(100, 100) #100,100 is the initial position
food1 = Food()
bfood = BFood()
tfood = TFood()

FPS = 60
d = 5
clock = pygame.time.Clock()
clock.tick(FPS)
running=True

#coбытие tfood_event повторяется каждые 5000 миллисекунд или 5 секунд
tfood_event = pygame.USEREVENT + 1 
pygame.time.set_timer(tfood_event, 5000)

while not snake.collision_check() and running:
    clock.tick(snake.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT and snake.dx != -d:
                snake.dx = d
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx != d:
                snake.dx = -d
                snake.dy = 0
            if event.key == pygame.K_UP and snake.dy != d:
                snake.dx = 0
                snake.dy = -d
            if event.key == pygame.K_DOWN and snake.dy != -d:
                snake.dx = 0
                snake.dy = d

        if event.type == tfood_event:
            tfood.gen() # каждые 5 секунд создается новая позиция для синей еды

    if snake.eat(food1.x, food1.y):
        snake.add_size = True
        food1.gen()

    if snake.eatBIG(bfood.x, bfood.y): 
        snake.add_size = True
        snake.add_sizeBIG = True #this additional boolean values are for identifying how many circles we need to add to our snake for this particular food
        bfood.gen()

    if snake.eatTime(tfood.x, tfood.y):
        snake.add_size = True
        snake.add_sizeTime = True
        tfood.gen()

    snake.move()

    screen.fill(green)

    screen.blit(snake.message1(), (10, 10))
    screen.blit(snake.message2(), (10, 30))
    screen.blit(snake.message3(), (10, 50))

    snake.draw()
    food1.draw()
    bfood.draw()
    tfood.draw()

    pygame.display.flip()
    
pygame.quit()