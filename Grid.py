#get modules
import math

#create grid object
class Grid:
    #initialise grid
    def __init__(self, size, screenSize):
        #hold screenSize
        self.screenSize = screenSize
        #set size of grid
        self.cellSize = size
        #use size to calculate num columns
        self.columns = math.ceil(screenSize[0] / self.cellSize)
        #use size to calculate num rows
        self.rows = math.ceil(screenSize[1] / self.cellSize)
        
        #make cell list
        self.cells = []
        
        #add lists to hold each particle once made
        for x in range(self.columns):
            #add each column to list
            self.cells.append([])
            for y in range(self.rows):
                #add each row to list
                self.cells[x].append([])
    
    #adds particle to grid cell
    def addParticle(self, particle):
        #works out column index
        col_idx = math.floor( particle.position[0] / self.cellSize)
        #works out row index
        row_idx = math.floor( particle.position[1] / self.cellSize)
        #check if column is invalid
        if col_idx >= len(self.cells):
            #set velocity to zero
            #particle.velocity = [0,0]
            #move particle back to safe area
            particle.position = [particle.position[0], 
                                 (len(self.cells)-1) * self.cellSize -10]
            #works out column index
            particle.position = [(len(self.cells)-1) * self.cellSize -10, 
                                 particle.position[1]]
            col_idx = math.floor( particle.position[0] / self.cellSize)
        elif col_idx <= -1:
            #set velocity to zero
            #particle.velocity = [0,0]
            #move particle back to safe area
            particle.position = [10, particle.position[1]]
            #works out column index
            col_idx = math.floor( particle.position[0] / self.cellSize)
        #check if row is invalid
        if row_idx >= len(self.cells[col_idx]):
            #set velocity to zero
            #particle.velocity = [0,0]
            #move particle back to safe area
            particle.position = [particle.position[0], 
                                 (len(self.cells[col_idx])-1) * self.cellSize -10]
            #works out row index
            row_idx = math.floor( particle.position[1] / self.cellSize)
        elif row_idx <= -1:
            #set velocity to zero
            #particle.velocity = [0,0]
            #move particle back to safe area
            particle.position = [particle.position[0], 10]
            #works out row index
            row_idx = math.floor( particle.position[1] / self.cellSize)

        #add particle to corresponding row and column in cells list
        self.cells[col_idx][row_idx].append(particle)
        #add updated info to particle class as dict
        particle.cell = { "column": col_idx, "row": row_idx }
      
    #removes particle from grid cell
    def removeParticle(self, particle):
        #works out column index
        col_idx = particle.cell["column"]
        #works out row index
        row_idx = particle.cell["row"]

        #get grid cell
        cell = self.cells[col_idx][row_idx]
        #get index of particle in cell
        arr_idx = cell.index(particle)
        #delete particle in cell
        del self.cells[col_idx][row_idx][arr_idx]

    #get a particle's neighbours
    def getNeighbors(self, particle, pygame, screen):
        #find top grid cell in top left using radius
        top_left = [
            math.floor((particle.position[0] - particle.radius) / self.cellSize),
            math.floor((particle.position[1] - particle.radius) / self.cellSize),
        ]
        #find top grid cell in bottom right using radius
        bottom_right = [
            math.floor((particle.position[0] + particle.radius) / self.cellSize),
            math.floor((particle.position[1] + particle.radius) / self.cellSize),
        ]
        #list of neighbours
        neighbors = []
        if particle.marker:
            #print(99999)
            pygame.draw.rect(screen, "blue", pygame.Rect(particle.position[0] - particle.radius, 
                                                     particle.position[1] - particle.radius, 
                                                     particle.radius*2, 
                                                     particle.radius*2))
        #double nested loop to iterate from left to right then top to bottom of selected area.
        for i in range(top_left[0], bottom_right[0] + 1):
            for j in range(top_left[1], bottom_right[1] + 1):
                #don't access grid cells that don't exist
                if i < 0 or j < 0 or i >= self.columns or j >= self.rows:
                    continue
                #get current cell from array
                cell = self.cells[i][j]
                #iterate over all particles in cell
                for p in cell:
                    #don't add the particle itself
                    #if p != particle:
                    #    #add neighbour
                    #    if particle.marker:
                    #        p.colour = "blue"
                    #    else:
                    #        p.colour = "red"
                        neighbors.append(p)
        
        return neighbors
    

    