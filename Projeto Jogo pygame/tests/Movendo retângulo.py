import pygame
from sys import exit

pygame.init()
Title = "Movimento"

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
vel = 25


# Loop

programa_rodando = True
while programa_rodando:  # Atualização constante da tela

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programa_rodando = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 800 - width:
        x += vel

    if keys[pygame.K_UP] and y > 0:
        y -= vel

    if keys[pygame.K_DOWN] and y < 600 - height:
        y += vel



    if x > 800 - width:
        x = 800 - width

    if x < 0:
        x = 0

    if y > 600 - height:
        y = 600 - height

    if y < 0:
        y = 0



    win.fill((0,0,0))
    pygame.draw.rect(win, (0,0,255), (x,y,width,height))


    pygame.display.update()
    clock.tick(60)
pygame.quit()