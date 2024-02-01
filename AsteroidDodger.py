import pygame
# import random

pygame.init()

fps = 60

clock = pygame.time.Clock()

white = (255, 255, 255)

WIDTH = 1800
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

icon = pygame.image.load("SpaceDodgerIcon.png")
BG = pygame.transform.scale(pygame.image.load("SpaceBackground.jpeg"), (WIDTH, HEIGHT))


def draw():
    screen.blit(BG, (0, 0))
    pygame.display.update()


pygame.display.set_caption("Space Dodger")

pygame.display.set_icon(icon)

draw()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
