import math

#draws all particles to screen
def drawParticles(particles, screen, pygame):
    #clear the screen
    screen.fill("black")
    #loop over all particles
    for particle in particles:
        #uses pygame function to draw particles
        colour = particle.colour
        l =particle.energy/10
        if l > 1:
            l = 1
        colour = pygame.Color(0,255,0).lerp((255,0,0),l)
        pygame.draw.circle(screen, colour, particle.position, particle.size)
    
    #shows screen to user
    pygame.display.flip()    

