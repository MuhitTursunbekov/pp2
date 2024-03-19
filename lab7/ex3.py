import pygame

pygame.init()

size=weight,height=(400,400)

RED=(255,0,0)
WHITE=(255,255,255)

screen=pygame.display.set_mode(size)

screen.fill(WHITE)

x=200
y=200



def Draw_Circle(x,y):
    screen.fill(WHITE)
    pygame.draw.circle(screen,RED,(x,y),25)

pygame.draw.circle(screen,RED,(x,y),25)

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
            y+=40
            
            if y>=400:
                y=20
                Draw_Circle(x,y)
            else:
                Draw_Circle(x,y)
        
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            y-=40
            if y<=0:
                y=380
                Draw_Circle(x,y)
            else:
                Draw_Circle(x,y)
            

        if  event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            x+=40
            if x>=400:
                x=20
                Draw_Circle(x,y)
            else:
                Draw_Circle(x,y)   
        if  event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            x-=40
            if x<=0:
                x=380
                Draw_Circle(x,y)
            else:
                Draw_Circle(x,y)

    pygame.display.update()      



pygame.quit()