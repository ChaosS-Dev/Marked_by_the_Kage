import pygame, sys

pygame.init()
Title = "Stick"
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption(Title)
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)


while True:  # Atualização constante da tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
