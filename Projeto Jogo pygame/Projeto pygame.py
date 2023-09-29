import pygame
from sys import exit

pygame.init()
Title = "Stick"

# Display
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption(Title)

clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)


while True:  # Atualização constante da tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
