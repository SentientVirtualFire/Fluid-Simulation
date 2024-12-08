#fetch modules
import math, Generator, numpy as np

#class defining particles
class Particle:
    #initialising the particles, not all properties are required immediately 
    def __init__(self, x, y, mass, viscosity, density, pressure = 0, 
                 cell = None, dx = 0, dy = 0, colour = "black", size = 1, radius = 0.5, marker = False):
        #particle's position
        self.position = [x,y]
        self.posMag = math.sqrt(x**2+y**2)
        #next position in system
        self.nextPos = [x,y]
        #particle fixed properties, mass/visco/densit/pressure
        self.mass = mass
        self.viscosity = viscosity
        self.density = density
        self.pressure = pressure
        #particle's velocity/change in position
        self.velocity = [dx,dy]
        #particle's assigned grid cell at start/ will vary
        self.cell = cell
        #particle's acceleration/change in velocity, set to zero, will change automatically
        self.accel = 0,0
        #superficial properties just for the drawing the particle later
        self.colour = colour
        #drawing size of particle
        self.size = size
        #interacting radius of particle
        self.radius = radius
        #is this particle being checked
        self.marker = marker
        #kinetic energy in particle
        self.energy = 0
    
    #update next position
    def update(self, neighbours, screenSize):
        #get gravity strength
        g = Generator.gravity
        #set acceleration
        Ax = 0.0001
        Ay = g
        #set "bounciness" of walls
        damping = 1
        #iterate over neighbours:
        for p in neighbours:
            #work out magnitude of distance between particles
            distMag = math.sqrt(math.fabs((p.position[0]- self.position[0])**2 + (p.position[1]- self.position[1])**2))
            #is it in range
            if distMag <= 1.5:
                #v = (m1u1 + m2u2)/(m1 + m2)   
                #magnitutde of velocity for both particles
                veloMag = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
                otherVeloMag = math.sqrt(p.velocity[0]**2 + p.velocity[1]**2)
                #total energy
                totEnergy = self.mass*veloMag**2 + p.mass*otherVeloMag**2
                #new velocity
                newV = (totEnergy/(self.mass+p.mass))**(0.5)
                #degree in radians between particles
                deg = math.atan2(p.position[1]- self.position[1],p.position[0]- self.position[0])
                #update new velocity
                self.velocity[0] = -(newV*math.cos(deg))
                self.velocity[1] = -(newV*math.sin(deg))
        
        #particle's kinetic energy
        #self.energy = self.mass * (self.velocity[0]**2 + self.velocity[1]**2)/2 + g*(screenSize[1]-self.position[1])
        self.energy = self.mass * (self.velocity[0]**2 + self.velocity[1]**2)
        #apply acceleration to velocity
        self.velocity[0] += Ax
        self.velocity[1] += Ay
        
        #update for next position
        self.nextPos[0] = self.position[0] + self.velocity[0]
        self.nextPos[1] = self.position[1] + self.velocity[1]
        

        #validate x to bounds based on screen size and 0
        if self.nextPos[0] > screenSize[0]:
            self.nextPos[0] = screenSize[0]-1
            self.velocity[0] = -self.velocity[0]/damping
        if self.nextPos[0] < 0:
            self.nextPos[0] = 0
            self.velocity[0] = -self.velocity[0]/damping
        #validate y to bounds based on screen size and 0
        if self.nextPos[1] > screenSize[1]:
            self.nextPos[1] = screenSize[1] -1 
            self.velocity[1] = -self.velocity[1]/damping
        if self.nextPos[1] < 0:
            self.nextPos[1] = 0
            self.velocity[1] = -self.velocity[1]/damping

    #calculate density mass/area
    def Density(self,neighbours):
        #get area to calculate density around
        area = self.radius**2*4
        #take sum of particles masses and divide it by area of search
        return sum([p.mass for p in neighbours])/area 
    
    
    #apply new position
    def applyUdt(self):
        self.position = self.nextPos
    

