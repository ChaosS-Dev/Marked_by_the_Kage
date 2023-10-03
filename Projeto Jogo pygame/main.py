import pygame, sys
from settings import *
from level import Level

pygame.init()
Title = "Stick"
screen_width, screen_height = 1200, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(Title)
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)
level = Level(level_map,screen)

while True:  # Atualização constante da tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    level.run()
    pygame.display.update()
    clock.tick(60)