#Importing all modules 
import math, Particle, pygame, Draw, Generator, Grid
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
particles = Generator.particleGeneration(particles)





#initialise grid
grid = Grid.Grid(50, screen.get_size())
#update grid positions
for p in particles:
    grid.addParticle(p)
#counts fps
fps = 0
#sets the program to started
running = True
#if running is False program will stop
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
        if event.type == pygame.KEYDOWN:
                #if the user presses the q button 
                #this part doesn't require the keys list as it is one item
                if event.key == pygame.K_q:
                    running = False
    
    #get all particles and calculate with their neighbours
    for p in particles:
        neighbours = grid.getNeighbors(p)
        p.update(neighbours)
    #apply all new positions
    for p in particles:
         p.applyUdt()
    #call module to draw particles
    Draw.drawParticles(particles, screen, pygame)
    #update grid positions
    for p in particles:
        grid.removeParticle(p)
        grid.addParticle(p)

    #takes time elapsed
    elapsed = timer() - start
    #calculates fps
    fps = 1/elapsed
    #logs fps
    print(fps)

