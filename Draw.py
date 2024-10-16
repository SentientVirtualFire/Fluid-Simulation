#draws all particles to screen
def drawParticles(particles, screen, pygame):
    #clear the screen
    screen.fill("white")
    #loop over all particles
    for particle in particles:
        #uses pygame function to draw particles
        pygame.draw.circle(screen, particle.colour, particle.position, particle.size)
    
    #shows screen to user
    pygame.display.flip()    

