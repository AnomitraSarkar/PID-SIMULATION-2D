
import matplotlib.pyplot as plt
import pygame

pygame.init() 
forcearr = []
win = pygame.display.set_mode((700, 700)) 
pygame.display.set_caption("Moving rectangle") 
x = 350
y = 700
ux = 0
uy = 0
ERROR_ENTER = 600
# dimensions of the object  
width = 10
height = 50
FPS = 60
intgerr = 0
setforcex = 0
dt = 1/FPS
m = 10
approx = 0.2

path=[(x+width/2,y),(x+width/2,y)]

height_rocket =  50
width_rocket = 20
force_y = -10
force_x = -2
preverr = setforcex - force_x

def rocket_loc(fx,fy) -> tuple:
    global x,y,ux,uy
    ax = fx/m
    ay = fy/m
    ux = ux - ax*dt
    uy = uy - ay*dt
    x -= ux*dt + (ax*dt*dt/2)
    y -= uy*dt + (ay*dt*dt/2)
    baseLeft = (x,y)
    bodyLeft = (x,y-height_rocket)
    arrow = (x+(width_rocket/2),y-(3*height_rocket/2))
    bodyRight = (x+width_rocket,y-height_rocket)
    baseRight = (x+width_rocket,y)
    make_line()
    return baseLeft, bodyLeft, arrow, bodyRight, baseRight
 
def make_line(): 
    path.append((x+width/2,y))
    forcearr.append(force_x)

def PID_KERNEL(err) -> int:
    global preverr, intgerr
    kp = 0.8
    ki = 0.086
    kd = 0.016
    perror = err
    intgerr += err*dt
    differr = (err - preverr) / dt
    preverr = err
    output = (kp*perror) - (ki * intgerr) + (kd * differr)
    return output

if __name__ == "__main__":
    
    run = True

    while run: 
        pygame.time.delay(10) 
        
        
        for event in pygame.event.get(): 
            
            if event.type == pygame.QUIT: 
                plt.plot(forcearr)
                plt.show()
                run = False
        
        
                
        win.fill((255,255 ,255)) 
        
        # drawing object on screen which is rectangle here  
        # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height),2)
        
        if( y>ERROR_ENTER-1  and y <ERROR_ENTER + 1) :
            print("Error induced")
            force_x = 100
            
        if(force_x != 0):
            # pass
            print(force_x)
            force_x = PID_KERNEL(force_x - setforcex)
        
            
        
        pygame.draw.polygon(win, (0, 0, 0), (rocket_loc(force_x,force_y)) )
        pygame.draw.polygon(win, (0, 0, 0), (path) )
        
        # it refreshes the window 
        pygame.display.update()  
    
    # closes the pygame window  
    pygame.quit() 

