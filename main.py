#Importing all modules 
import math, Particle, pygame


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

#default particle count, may adjust
particleCount = 1000
particleMass = 1
particleViscosity = 1
particleDensity = 1
posRange = [(10,500),(10,500)]

#load all particles
def particleGeneration():
    particles = []

    #temporary variable to work out factors
    factor = round(math.sqrt(particleCount))
    #work out closest factors
    while particleCount%factor > 0: 
        factor -= 1
    #number of particles in each row in column
    rowCount = factor
    columnCount = particleCount//factor

    for x in rowCount:
         xPos = posRange[1][0]
         for y in columnCount:
              yPos = posRange[1][0]

              particle = Particle.Particle(
                   xPos,
                   yPos,
                   particleMass,
                   particleViscosity,
                   particleDensity)
              particles.append(particle)

              yPos += (posRange[1][1] - posRange[1][0])/columnCount
        
         xPos += (posRange[0][1] - posRange[0][0])/columnCount







#sets the program to started
running = True
#if running is False program will stop
while running:
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

        