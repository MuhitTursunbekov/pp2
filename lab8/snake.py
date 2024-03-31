import pygame, sys, random, time
pygame.init()

FPS = pygame.time.Clock() #Make game slow
fps = 10
FPS.tick(fps)

White = (255, 255, 255)
LightSteelBlue = (176, 196, 222)
Red = (255, 0, 0)
Green = (0, 255, 0) #Colors

height = 500
width = 500
window = (width, height)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Lab8 Snake") #Window settings
step = 20

direction = 'RIGHT'

End = False 
append = False 

background=pygame.transform.scale(pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab8\background.png'),(600,600)) 
coin=pygame.transform.scale(pygame.image.load(r'C:\Users\User\OneDrive\Рабочий стол\pp2\lab8\coin.png'),(20,20)) 
font=pygame.font.SysFont('Times New Roman', 24)
score=0  
body=[] #body as array
head_x = head_y=240
step=20 
move_x,move_y=20,0 #first speed
direction =  'RIGHT' #first direction

def rand():
    return(random.randint(2,22)*20) #random coin spawn

coin_x=rand()
coin_y=rand()

while True:
    FPS.tick(fps)
    pressed = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type==pygame.QUIT or pressed[pygame.K_SPACE]:
            pygame.quit()
            sys.exit() 


        if pressed[pygame.K_DOWN]: 
            if direction!='UP': 
                direction= 'DOWN' 
                move_x= 0 
                move_y= step 

        if pressed[pygame.K_UP]: 
            if direction!='DOWN':
                direction = 'UP'
                move_x = 0
                move_y = -step

        if pressed[pygame.K_LEFT]:
            if direction!='RIGHT':
                direction = 'LEFT'
                move_x = -step
                move_y = 0

        if pressed[pygame.K_RIGHT]: 
            if direction!='LEFT':
                direction = 'RIGHT'
                move_x = step
                move_y = 0    #Head movement directions

        
    if not End:    
        body.append([head_x,head_y]) 
        body.pop(0) 
        if append:
            body.append([head_x,head_y])  #body increase
            score+=1 
            append=False
        head_x+=move_x 
        head_y+=move_y



        if head_x<0 or head_x>480 or head_y<0 or head_y>480: #inside the borders
            End=True 


        fps=10+ score #make faster
        while head_x==coin_x and head_y==coin_y:
            coin_x=rand()
            coin_y=rand()
            append=True
        screen.blit(background,(0, 0)) 
        screen.blit(coin,(coin_x,coin_y))
        pygame.draw.rect(screen,(0, 100, 0),(head_x,head_y,20,20))

        for block in body:
        

            while block[0]==coin_x and block[1]==coin_y:    
                coin_x=rand()
                coin_y=rand()
            if head_x==block[0] and head_y==block[1]: 
                End=True 
                break 
            pygame.draw.rect(screen,(0,200,0),(block[0],block[1],20,20)) 
            screen.blit(font.render("Score: {}".format(score),True,(255,0,0)), (10,10)) 
    else: 
        screen.fill((255,255,255)) 
        screen.blit(font.render("GAME OVER",True,(255,0,0)),(175,200))  #Game Over
    pygame.display.update() 