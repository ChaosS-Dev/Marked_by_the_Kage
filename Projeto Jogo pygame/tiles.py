import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, posicao, tamanho):
        super().__init__()
        self.image = pygame.Surface((tamanho, tamanho))
        self.image.fill('Red')
        self.rect = self.image.get_rect(topleft=posicao)

    def update(self, deslocamento_x):
        self.rect.x += deslocamento_x