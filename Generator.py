#get modules
import Particle, math

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

    #iterate over all rows and columns
    #range: starting x position, end x position, step for each num in row count
    for xPos in range(posRange[0][0],
                      posRange[0][1],
                      (posRange[0][1] - posRange[0][0])/rowCount):

        #range: starting y position, end y position, step for each num in column count
        for yPos in range(posRange[1][0], 
                          posRange[1][1], 
                          (posRange[1][1] - posRange[1][0])/columnCount):
            
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