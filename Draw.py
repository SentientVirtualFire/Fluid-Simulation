import math, Generator

#draws ui to screen
def drawUI(screen, pygame, fps, font):
    #create text object to draw to screen
    txts = [f"FPS: {round(fps,1)}",
            f"Density: {Generator.particleDensity}",
            f"Gravity: {Generator.gravity}",
            f"Pressure: {Generator.particlePressure}",
            f"Viscosity: {Generator.particleViscosity}",]
    #rounding the fps value as actual number is approx to 10 decimal places
    #which isnt providing useful data 
    #rendered texts
    renders = [font.render(t, True, "white") for t in txts]
    #drawing the text to the screen in a loop
    for line in range(len(renders)):
        #positioning the text onscreen
        screen.blit(renders[line],(10,10+(line*font.get_height())+(10*line)))

#draws all particles to screen
def drawParticles(particles, screen, pygame, max, min, mean):
    #clear the screen
    max = max
    min = min
    #loop over all particles
    for particle in particles:
        colour = particle.colour
        if particle.colour != "white":
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
        #    particle.colour = "pink"
        #if particle == particles[0]:
        #    particle.colour = "black"
        pygame.draw.circle(screen, colour, particle.position, particle.size)
    
    #shows screen to user
    pygame.display.flip()   

