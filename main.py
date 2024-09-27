import math, pygame



pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
winDimensions = screen.get_size()
fps = 60
font = pygame.font.SysFont('chalkduster.ttf', 40)

