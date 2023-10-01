import pygame
from sys import exit

pygame.init()
Title = "Colisões"

# Display
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption(Title)

clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)


# Config. do retângulo

# Coordenadas

x1 = 200
y1 = 200

x2 = 400
y2 = 300

# Dimensões
width1 = 40
height1 = 40

width2 = 30
height2 = 15

# Velocidade
vel_x1 = 15
vel_y1 = 10

vel_x2 = 10
vel_y2 = 20

# Loop

programa_rodando = True
while programa_rodando:  # Atualização constante da tela

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programa_rodando = False

    keys = pygame.key.get_pressed()

    x1 += vel_x1
    y1 += vel_y1

    x2 += vel_x2
    y2 += vel_y2

# Colisão com a janela

    if y1 > 600 - width1:
        vel_y1 = -vel_y1


    if y1 < 0:
        vel_y1 = -vel_y1


    if x1 > 800 - height1:
        vel_x1 = -vel_x1


    if x1 < 0:
        vel_x1 = -vel_x1



    if y2 > 600 - width2:
        vel_y2 = -vel_y2

    if y2 < 0:
        vel_y2 = -vel_y2



    if x2 > 800 - height2:
        vel_x2 = -vel_x2

    if x2 < 0:
        vel_x2 = -vel_x2



# Colisões entre si














    win.fill((0,0,0))
    pygame.draw.rect(win, (0,0,255), (x1,y1,width1,height1))
    pygame.draw.rect(win, (255, 0, 0), (x2, y2, width2, height2))


    pygame.display.update()
    clock.tick(60)
pygame.quit()