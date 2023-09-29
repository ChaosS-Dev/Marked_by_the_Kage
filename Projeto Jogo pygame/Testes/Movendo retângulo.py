import pygame
from sys import exit

pygame.init()
Title = "Stick"

# Display
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption(Title)

clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)


# Config. do retângulo

# Coordenadas

x = 200
y = 200

# Dimensões
width = 20
height = 20

# Velocidade
vel = 10


# Loop

programa_rodando = True
while programa_rodando:  # Atualização constante da tela
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programa_rodando = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel

    if keys[pygame.K_UP] and x > 0:
        x -= vel

    if keys[pygame.K_DOWN] and x < 500 - height:
        x += vel

    pygame.display.update()
    clock.tick(60)
