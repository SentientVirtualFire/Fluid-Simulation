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