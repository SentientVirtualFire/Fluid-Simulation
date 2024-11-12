#get modules
import Particle, math


#default mass
particleMass = 1
#default viscosity
particleViscosity = 1
#default density
particleDensity = 1
#the range of x and y positions over which the particles will be produced
posRange = ((50,500),(50,500))
#gravitational constant
gravity = 0.001

#load all particles
def particleGeneration(particles):
    #default particle count
    particleCount = 1000
    #check particleCount is in allowed range
    if particleCount > 10000:
        particleCount = 10000
    if particleCount < 2:
        particleCount = 2
    #check particleCount is in allowed type
    if type(particleCount) != type(4):
        raise TypeError

    #temporary variable to work out factors
    factor = round(math.sqrt(particleCount))
    #work out closest factors
    while particleCount%factor > 0: 
        factor -= 1
    #number of particles in each row in column
    rowCount = factor
    columnCount = particleCount//factor

    #iterate over all rows and columns
    #range: starting x position, end x position, step for each num in row count
    for xPos in range(posRange[0][0]*rowCount,
                      posRange[0][1]*rowCount,
                      posRange[0][1] - posRange[0][0]):
        #readjust x position value
        xPos /= rowCount
        #range: starting y position, end y position, step for each num in column count
        for yPos in range(posRange[1][0]*columnCount, 
                          posRange[1][1]*columnCount, 
                          posRange[1][1] - posRange[1][0]):
            #readjust y position value
            yPos /= columnCount
            #instantiate particle class at this position
            particle = Particle.Particle(
                xPos,
                yPos,
                particleMass,
                particleViscosity,
                particleDensity)
            #add to list of particles
            particles.append(particle)
            
    #returns the generated list of particles
    return particles