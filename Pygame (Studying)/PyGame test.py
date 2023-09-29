import pygame
from sys import exit

pygame.init()
Title = "Pytonho"


screen = pygame.display.set_mode((800, 600))  # 800 = Largura, 600 = Altura
pygame.display.set_caption(Title)

pygame_icon = pygame.image.load("Test.png")
pygame.display.set_icon(pygame_icon)

clock = pygame.time.Clock()
text_font = pygame.font.Font(
    "font/Pixeltype.ttf", 50
)  # (tipo de fonte {None é o padrão do pygame}, tamanho da fonte)
text_surface = text_font.render(
    "Meu joguinho", True, "Black"
)  # (Texto, Suavizar as bordas {true/false}, cor do texto)


"""test_surface = pygame.Surface((100,300)) # Largura e altura
test_surface.fill('Blue') # Definir cor da superfície"""  # Usamos isso para um cenário no próprio display (sem imagens)


sky_surface = pygame.image.load(
    "graphics/Sky.png"
).convert()  ##--- Falta terminar o comando
sky_surface = pygame.transform.scale(sky_surface, (900, 500))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_x_pos = 600
snail_y_pos = 415


ground_surface = pygame.image.load("graphics/ground.png")
while True:  # O while será responsável pelo loop (atualização constante da tela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))  # Superfície (test_surface) e posição (0,0)
    screen.blit(ground_surface, (0, 450))
    screen.blit(text_surface, (300, 100))

    snail_x_pos -= 2
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, snail_y_pos))

    pygame.display.update()
    clock.tick(60)
