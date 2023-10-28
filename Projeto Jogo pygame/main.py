import pygame, sys
from configs import *
from level import Level

pygame.init()
Titulo = "Stick"
largura_display, altura_display = 1280, 720
display = pygame.display.set_mode((largura_display, altura_display))
pygame.display.set_caption(Titulo)
clock = pygame.time.Clock()
fonte_texto = pygame.font.Font(None, 50)
level = Level(mapa_level, display)

while True:  # Atualização constante da tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    display.fill((30,30,30))
    level.run()
    pygame.display.update()
    clock.tick(60)