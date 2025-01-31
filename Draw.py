import math

#draws all particles to screen
def drawParticles(particles, screen, pygame, max, min, mean):
    #clear the screen
    screen.fill("black")
    max = max
    min = min
    #loop over all particles
    for particle in particles:
        if particle.energy > mean:
            weightedEnergy = (particle.energy-mean)/(max-mean + 0.000001)
            colour = pygame.Color(255,200,0).lerp((255,0,0),weightedEnergy)
        else:
            weightedEnergy = (particle.energy-min)/(mean-min + 0.000001)
            colour = pygame.Color(0,255,0).lerp((255,200,0),weightedEnergy)
        #limit weightedEnergy from being too high
        #interpolate between green and red based on speed
        #uses pygame function to draw particles
        #if particle.marker:
        #    particle.colour = "green"
        pygame.draw.circle(screen, colour, particle.position, particle.size)
    
    #shows screen to user
    pygame.display.flip()   

