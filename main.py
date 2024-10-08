#Importing all modules 
import math, Particle, pygame, Draw
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
#default particle count
particleCount = 1000
#default mass
particleMass = 1
#default viscosity
particleViscosity = 1
#default density
particleDensity = 1
#the range of x and y positions over which the particles will be produced
posRange = ((10,500),(10,500))

#load all particles
def particleGeneration(particles):

    #temporary variable to work out factors
    factor = round(math.sqrt(particleCount))
    #work out closest factors
    while particleCount%factor > 0: 
        factor -= 1
    #number of particles in each row in column
    rowCount = factor
    columnCount = particleCount//factor

    #starting x position
    xPos = posRange[1][0]
    #iterate over all rows and columns
    for x in rowCount:
        #starting y position
        yPos = posRange[1][0]
        for y in columnCount:
            #instantiate particle class at this position
            particle = Particle.Particle(
                xPos,
                yPos,
                particleMass,
                particleViscosity,
                particleDensity)
            #add to list of particles
            particles.append(particle)
            #increment y position by fixed amount
            yPos += (posRange[1][1] - posRange[1][0])/columnCount
        
        #increment x position by fixed amount
        xPos += (posRange[0][1] - posRange[0][0])/rowCount
    #returns the generated list of particles
    return particles






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
    
    #call module to draw particles
    Draw.drawParticles(particles, screen, pygame)

    #takes time elapsed
    elapsed = timer() - start
    #calculates fps
    fps = 1/elapsed
    #logs fps
    print(fps)

