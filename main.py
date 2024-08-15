import pygame

pygame.init() 
win = pygame.display.set_mode((700, 700)) 
pygame.display.set_caption("Moving rectangle") 
x = 350
y = 700
ERROR_ENTER = 600
ERROR_ALGO = 575
# dimensions of the object  
width = 10
height = 50
FPS = 30  
intgerr = 0
setvelx = 0
dt = 1/FPS

path=[(x+width/2,y),(x+width/2,y)]
# velocity / speed of movement 
vely = 1 #1000m/s
velx = 0 #100m/s

height_rocket =  50
width_rocket = 20

preverr = setvelx - velx


def rocket_loc(xvel,yvel) -> tuple:
    global x,y
    x-=xvel
    y-=yvel
    
    
    baseLeft = (x,y)
    bodyLeft = (x,y-height_rocket)
    arrow = (x+(width_rocket/2),y-(3*height_rocket/2))
    bodyRight = (x+width_rocket,y-height_rocket)
    baseRight = (x+width_rocket,y)
    make_line()
    return baseLeft, bodyLeft, arrow, bodyRight, baseRight
  
def ALGO(err) -> int:
    global preverr, intgerr
    kp = 0.1
    ki = 0.1
    kd = 0.01
    perror = err
    intgerr += err*dt
    differr = (err - preverr) / dt
    preverr = err
    output = (kp*perror) + (ki * intgerr) + (kd * differr)
    return output
 
def make_line(): 
    path.append((x+width/2,y))
    

if __name__ == "__main__":
    run = True

    while run: 
        pygame.time.delay(10) 
        
        
        for event in pygame.event.get(): 
            
            if event.type == pygame.QUIT: 
                
                run = False
        
        
                
        win.fill((255,255 ,255)) 
        
        # drawing object on screen which is rectangle here  
        # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height),2)
        
        if y==ERROR_ENTER :
            velx = 0.850
            
        
        if (y < ERROR_ALGO and velx != 0):
           err = setvelx - velx
           velx = ALGO(err)
            
        
        pygame.draw.polygon(win, (0, 0, 0), (rocket_loc(velx,vely)) )
        pygame.draw.polygon(win, (0, 0, 0), (path) )
        
        # it refreshes the window 
        pygame.display.update()  
    
    # closes the pygame window  
    pygame.quit() 