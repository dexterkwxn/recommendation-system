import math
import pygame
from info import *

def show_image(filename, circles, color, circles2, color2):
    pygame.init()
    # load image
    pygame.display.set_caption('image')
    img = pygame.image.load(filename)

    # scale image
    width = img.get_width()
    height = img.get_height()
    x = 800
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
        pygame.draw.circle(surface, color, (c[0] * x / 1000, c[1] * y / 1000), radius, thickness)
    for k, c in circles2.items():
        pygame.draw.circle(surface, color2, (c[0] * x / 1000, c[1] * y / 1000), radius, thickness)

    # render
    scrn = pygame.display.set_mode(img.get_size())
    scrn.blit(surface, (0, 0))
    pygame.display.update()

    status = True
    print("\nPress any key to continue.\n")
    while status:
        for i in pygame.event.get():
            if i.type == pygame.QUIT or i.type == pygame.KEYDOWN:
                status = False
    pygame.quit()


def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# show_image('./ntu_map.png', school_locations, (255, 0, 0))
# show_image('./ntu_map.png', hall_locations, (0, 255, 0))
