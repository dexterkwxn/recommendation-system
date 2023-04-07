import math
import pygame

def show_image(filename):
    pygame.init()
    x = 600
    # load image
    pygame.display.set_caption('image')
    img = pygame.image.load(filename)

    # scale image
    width = img.get_width()
    height = img.get_height()
    y = x * height / width;
    IMAGE_SZ = (x, y)

    # set up screen 
    scrn = pygame.display.set_mode((x, y))
    img = pygame.transform.scale(img, IMAGE_SZ)
    img = img.convert()

    # render
    scrn.blit(img, (0, 0))
    pygame.display.flip()
    status = True
    while (status):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                status = False
    pygame.quit()


def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

show_image('./image1.jpg')