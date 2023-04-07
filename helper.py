import math
import pygame
from info import *

def show_image(filename, circles):
    pygame.init()
    x = 800
    # load image
    pygame.display.set_caption('image')
    img = pygame.image.load(filename)

    # scale image
    width = img.get_width()
    height = img.get_height()
    y = x * height / width;
    IMAGE_SZ = (x, y)

    # set up screen 
    img = pygame.transform.scale(img, IMAGE_SZ)
    surface = pygame.Surface(img.get_size())
    surface.blit(img, (0, 0))

    # set up circle
    radius = 30
    thickness = 2
    for k, c in circles.items():
        pygame.draw.circle(surface, (255, 0, 0), (c[0] * x / 1000, c[1] * y / 1000), radius, thickness)

    # render
    scrn = pygame.display.set_mode(img.get_size())
    scrn.blit(surface, (0, 0))
    pygame.display.update()

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()


def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

show_image('./ntu_map.png', map_locations)