import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, posicao, tamanho,tipo):
        super().__init__()
        self.image = pygame.image.load(f"./levels/tile_sets/Texture/{tipo}.png")
        #self.image = pygame.Surface((tamanho,tamanho))
        # self.image.fill((69,117,222))

        self.rect = self.image.get_rect(topleft=posicao)

    def update(self, deslocamento_x, deslocamento_y):
        self.rect.x += deslocamento_x
        self.rect.y += deslocamento_y


class TileEstatico(Tile):
    def __init__(self, posicao, tamanho, superficie):
        super().__init__(posicao, tamanho)
        self.image = superficie