#get modules
import math

#create grid object
class Grid:
    #initialise grid
    def __init__(self, size, screenSize):
        #set size of grid
        self.cellSize = size
        #use size to calculate num columns
        self.columns = math.ceil(screenSize[0] / cellSize)
        #use size to calculate num rows
        self.rows = math.ceil(screenSize[1] / cellSize)
        
        #make cell list
        self.cells = []
        
        #add lists to hold each particle once made
        for x in range(columns):
            #add each column to list
            self.cells.append([])
            for y in range(rows):
                #add each row to list
                self.cells[x].append([])
    
    #adds particle to grid cell
    def addParticle(self, particle):
        #works out column index
        col_idx = math.floor( particle.pos[0] / this.cellSize)
        #works out row index
        row_idx = math.floor( particle.pos[1] / this.cellSize)

        #add particle to corresponding row and column in cells list
        self.cells[col_idx][row_idx].append(particle)
        #add updated info to particle class as dict
        particle.cell = { "column": col_idx, "row": row_idx }
      
    #removes particle from grid cell
    def removeParticle(self, particle):
        #works out column index
        col_idx = particle.gridCell["column"]
        #works out row index
        row_idx = particle.gridCell["row"]

        #get grid cell
        cell = self.cells[col_idx][row_idx]
        #get index of particle in cell
        arr_idx = cell.index(particle)
        #delete particle in cell
        del self.cells[col_idx][row_idx][arr_idx]

    #get a particle's neighbours
    def getNeighbors(self, particle):
        #find top grid cell in top left using radius
        top_left = [
            math.floor((particle.pos[0] - particle.radius) / self.cellSize),
            math.floor((particle.pos[1] - particle.radius) / self.cellSize),
        ]
        #find top grid cell in bottom right using radius
        bottom_right = [
            math.floor((particle.pos[0] + particle.radius) / self.cellSize),
            math.floor((particle.pos[1] + particle.radius) / self.cellSize),
        ]
        #list of neighbours
        neighbors = []

        #double nested loop to iterate from left to right then top to bottom of selected area.
        for i in range(top_left[0], bottom_right[0] + 1):
            for j in range(top_left[1], bottom_right[1] + 1):
                #don't access grid cells that don't exist
                if i < 0 or j < 0 or i >= self.numCols or j >= self.numRows:
                    continue
                #get current cell from array
                cell = self.cells[i][j]
                #iterate over all particles in cell
                for p in cell:
                    #don't add the particle itself
                    if p != particle:
                        #add neighbour
                        neighbors.append(p)
        
        return neighbors
    

    