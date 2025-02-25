#Importing all modules 
import math, Particle, pygame, Draw, Generator, Grid, matplotlib.pyplot as plt
from timeit import default_timer as timer

#initialise the pygame gui system
pygame.init()
#makes the screen variable to draw all the particles 
#and aligns the top left corner as 0,0 with full screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#sets the system clock for initialising the pygame library
clock = pygame.time.Clock()
#dimensions of the windows
winDimensions = screen.get_size()
#the font for the GUI
font = pygame.font.SysFont('chalkduster.ttf', 40)

#list of all particles
particles = []
#load all particles into function
particles = Generator.particleGeneration(particles, screen)





#initialise grid
numCells = 64
grid = Grid.Grid(numCells, screen.get_size())
#update grid positions
for p in particles:
    grid.addParticle(p)
#counts fps
fps = 0
#sets the program to started
running = True
#if running is False program will stop
kes = []
kes2 = []
max = 1
min = 1
while running:
    #takes current time
    start = timer()
    #holds all the keys pressed this frame/iteration
    keys = pygame.key.get_pressed()
    #iiterates all events pygame has proccessed, including keypresses
    for event in pygame.event.get():
        #if the program has been quit automatically or the user presses x button
        if event.type == pygame.QUIT:
            running = False
        #if the user presses any key
        if event.type == pygame.KEYDOWN :
                #if the user presses the q button 
                #this part doesn't require the keys list as it is one item
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_p:
                    plt.plot(range(len(kes)),kes)
                    plt.show()
                if event.key == pygame.K_i:
                    for i in particles:
                        i.pressure /= 10
                        print(i.pressure)
                if event.key == pygame.K_o:
                    for i in particles:
                        i.pressure *= 10
                        print(i.pressure)
    tot = 0
    #get all particles and calculate with their neighbours
    for p in particles:
        neighbours = grid.getNeighbors(p, pygame, screen)
        p.update(neighbours, screen.get_size(), numCells)
    #apply all new positions
    for p in particles:
        tot += p.energy
        p.applyUdt()
        p.localDensity = 0
         
        if p.energy > max:
            max = p.energy
        if p.energy < min:
            min = p.energy
    mean = tot / len(particles)
    #call module to draw particles
    screen.fill("black")
    screenSize = screen.get_size()
    if 0:
        for x in range(screenSize[0]):
            for y in range(screenSize[1]):
                if math.ceil(x % (screenSize[0] / numCells))==0 or math.ceil(y % (screenSize[1] / numCells))==0:
                    pygame.draw.circle(screen, (16,16,16), (x,y), 1)
                #pass
                #print(1,x,y)
    Draw.drawParticles(particles, screen, pygame, max, min, mean)
    #update grid positions
    for p in particles:
        grid.removeParticle(p)
        grid.addParticle(p)
    max = 1
    min = 1
    
    pygame.display.flip()     
    #takes time elapsed
    elapsed = timer() - start
    #calculates fps
    fps = 1/elapsed
    #logs fps
    kes2.append(sum(kes)/(len(kes)+1))
    #print(fps, tot, kes2[-1:])
    kes.append(tot)
    #print(len(particles))
