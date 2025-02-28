#Importing all modules 
import math, Particle, pygame, Draw, Generator, Grid, matplotlib.pyplot as plt
from timeit import default_timer as timer

#initialise the pygame gui system
pygame.init()
#makes the screen variable to draw all the particles 
#and aligns the top left corner as 0,0 with full screen
screen = pygame.display.set_mode((0, 0))
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

#resets simulation
def Reset(grid, particles):
    #empties grid
    for p in particles:
        grid.removeParticle(p)
    #list of all particles
    particles = []
    #load all particles into function
    particles = Generator.particleGeneration(particles, screen)
    #add particles back to grid
    for p in particles:
        grid.addParticle(p)
    return grid, particles

while running:
    #takes current time
    start = timer()
    #holds all the keys pressed this frame/iteration
    keys = pygame.key.get_pressed()

    #increase density when d+up pressed
    if keys[pygame.K_d] and keys[pygame.K_UP]:
        Generator.particleDensity *= 1.1
    #decrease density when d+down pressed
    if keys[pygame.K_d] and keys[pygame.K_DOWN]:
        Generator.particleDensity /= 1.1
    #change pressure
    if keys[pygame.K_p] and keys[pygame.K_UP]:
        Generator.particlePressure *= 1.1
    if keys[pygame.K_p] and keys[pygame.K_DOWN]:
        Generator.particlePressure /= 1.1
    #change viscosity
    if keys[pygame.K_v] and keys[pygame.K_UP]:
        Generator.particleViscosity *= 1.1
    if keys[pygame.K_v] and keys[pygame.K_DOWN]:
        Generator.particleViscosity /= 1.1
    #change gravity
    if keys[pygame.K_g] and keys[pygame.K_UP]:
        Generator.gravity *= 1.1
    if keys[pygame.K_g] and keys[pygame.K_DOWN]:
        Generator.gravity /= 1.1

    #iiterates all events pygame has proccessed, including keypresses
    for event in pygame.event.get():
        #if the program has been quit automatically or the user presses x button
        if event.type == pygame.QUIT:
            running = False
        #if the user presses any key
        if event.type == pygame.KEYDOWN :
                #this part doesn't require the keys list as it is one item
                #if the user presses the q button 
                #quit
                if event.key == pygame.K_q:
                    running = False
                #draw debugging plot
                if event.key == pygame.K_o:
                    plt.plot(range(len(kes)),kes)
                    plt.show()
                #reset
                if event.key == pygame.K_r:
                    grid, particles = Reset(grid, particles)
                
                #if key is pressed validate viscosity for range
                if Generator.particleViscosity > 1e-10:
                    Generator.particleViscosity = 1e-10
                if Generator.particleViscosity < 1e-14:
                    Generator.particleViscosity = 1e-14
                #validate pressure
                if Generator.particlePressure < 1e-15:
                    Generator.particlePressure = 1e-15
                if Generator.particlePressure > 1e-8:
                    Generator.particlePressure = 1e-8
                #validate density
                if Generator.particleDensity < 0:
                    Generator.particleDensity = 1e-6
                #validate types
                if type(Generator.particleDensity) != type(0.1):
                    Generator.particleDensity = 1
                if type(Generator.particlePressure) != type(0.1):
                    Generator.particlePressure = 1e-10
                if type(Generator.particleViscosity) != type(0.1):
                    Generator.particleViscosity = 1e-12
                if type(Generator.gravity) != type(0.1):
                    Generator.gravity = 0.5

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
    
    #draw ui features
    Draw.drawUI(screen,pygame,fps,font)
    #draw particles to relevant positions
    Draw.drawParticles(particles, screen, pygame, max, min, mean)
    #update grid positions
    for p in particles:
        grid.removeParticle(p)
        grid.addParticle(p)
    max = 1
    min = 1
    
    #debugging energy calculations
    kes2.append(sum(kes)/(len(kes)+1))
    kes.append(tot)
    #takes time elapsed
    elapsed = timer() - start
    #calculates fps
    fps = 1/elapsed
    clock.tick(60)

