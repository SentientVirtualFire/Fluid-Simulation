#class defining particles
class Particle:
    #initialising the particles, not all properties are required immediately 
    def __init__(self, x, y, mass, viscosity, density, pressure = 0, 
                 cell = None, dx = 0, dy = 0, colour = "black", size = 1):
        #particle's position
        self.position = x,y
        #particle fixed properties, mass/visco/densit/pressure
        self.mass = mass
        self.viscosity = viscosity
        self.density = density
        self.pressure = pressure
        #particle's velocity/change in position
        self.velocity = dx,dy
        #particle's assigned grid cell at start/ will vary
        self.cell = cell
        #particle's acceleration/change in velocity, set to zero, will change automatically
        self.accel = 0,0
        #superficial properties just for the drawing the particle later
        self.colour = colour
        self.size = size

