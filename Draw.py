import math

#draws all particles to screen
def drawParticles(particles, screen, pygame, max, min):
    newmax, newmin = 0,0
    #clear the screen
    screen.fill("black")
    #loop over all particles
    for particle in particles:
        #get particle's energy
        if particle.energy > newmax:
            newmax = particle.energy
        if particle.energy < newmin:
            newmin = particle.energy
        weightedEnergy = (particle.energy-min)/(max-min + 0.000001)
        #limit weightedEnergy from being too high
        if weightedEnergy > 1:
            weightedEnergy = 1
        if weightedEnergy < 0:
            weightedEnergy = 0
        #interpolate between green and red based on speed
        colour = pygame.Color(0,255,0).lerp((255,0,0),weightedEnergy)
        #uses pygame function to draw particles
        pygame.draw.circle(screen, colour, particle.position, particle.size)
    
    #shows screen to user
    pygame.display.flip()    
    return max,min

