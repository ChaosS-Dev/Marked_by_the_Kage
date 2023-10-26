import pygame
from tiles import Tile
from configs import tamanho_tile, largura_display
from jogador import Jogador


class Level:
    def __init__(self, level_data, superficie):
        self.display_surface = superficie
        self.setup_level(level_data)

        self.deslocamento_level_x = 0  # Movimento do level

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.jogador = pygame.sprite.GroupSingle()
        for index_linha, linha in enumerate(layout):
            for index_coluna, celula in enumerate(linha):
                if celula == 'X':
                    x = index_coluna * tamanho_tile
                    y = index_linha * tamanho_tile
                    tile = Tile((x, y), tamanho_tile)  # Posição (x,y); Tamanho (tile_size de settings, padrão = 64)
                    self.tiles.add(tile)
                if celula == 'P':
                    x = index_coluna * tamanho_tile
                    y = index_linha * tamanho_tile
                    sprite_jogador = Jogador((x, y))  # Posição (x,y); Tamanho (tile_size de settings, padrão = 64)
                    self.jogador.add(sprite_jogador)

    def scroll_x(self):
        jogador = self.jogador.sprite
        jogador_x = jogador.rect.centerx
        direcao_x = jogador.direcao.x
        keys = pygame.key.get_pressed()

        if keys[pygame.K_x]:
            if jogador_x < largura_display / 4 and direcao_x < 0:
                self.deslocamento_level_x = jogador.velocidade_level
                jogador.velocidade = 0
            elif jogador_x > largura_display - (largura_display / 4) and direcao_x > 0:
                self.deslocamento_level_x = -jogador.velocidade_level
                jogador.velocidade = 0
            else:
                self.deslocamento_level_x = 0

        elif not keys[pygame.K_x]:
            if jogador_x < largura_display / 4 and direcao_x < 0:
                self.deslocamento_level_x = jogador.velocidade_inicial
                jogador.velocidade = 0
            elif jogador_x > largura_display - (largura_display / 4) and direcao_x > 0:
                self.deslocamento_level_x = -jogador.velocidade_inicial
                jogador.velocidade = 0
            else:
                self.deslocamento_level_x = 0
                jogador.velocidade = jogador.velocidade_inicial

    def colisao_movimento_horizontal(self):  # Colisões laterais com os tiles
        jogador = self.jogador.sprite
        jogador.rect.x += jogador.direcao.x * jogador.velocidade
        tolerancia_colisao = 50

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(jogador.rect):  # Colisão de parede com jogador
                if jogador.direcao.x < 0 and abs(jogador.rect.left - sprite.rect.right) < tolerancia_colisao:
                    jogador.rect.left = sprite.rect.right
                    jogador.colisao_esquerda = True
                    jogador.direcao.x = 0


                elif jogador.direcao.x > 0 and abs(jogador.rect.right - sprite.rect.left) < tolerancia_colisao:
                    jogador.rect.right = sprite.rect.left
                    jogador.colisao_direita = True
                    jogador.direcao.x = 0


    def colisao_movimento_vertical(self):
        jogador = self.jogador.sprite
        tolerancia_colisao = 50
        jogador.aplicar_gravidade()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(jogador.rect):  # Colisão de parede com jogador
                if jogador.direcao.y > 0 and abs(jogador.rect.bottom - sprite.rect.top) < tolerancia_colisao:
                    jogador.rect.bottom = sprite.rect.top
                    jogador.direcao.y = 0
                    jogador.colisao_chao = True


                elif jogador.direcao.y < 0 and abs(jogador.rect.top - sprite.rect.bottom) < tolerancia_colisao:
                    jogador.rect.top = sprite.rect.bottom
                    jogador.direcao.y = 0
                    jogador.colisao_topo = True
        if jogador.colisao_chao and jogador.direcao.y < 0 or jogador.direcao.y > 1: # Registro de colisão com o chão
            jogador.colisao_chao = False

        if jogador.colisao_topo and jogador.direcao.y > 0:  # Registro de colisão com o teto
            jogador.colisao_topo = False
    def sem_colisao_vertical(self):
        jogador = self.jogador.sprite
        jogador.colisao_topo = False
        jogador.colisao_chao = False

    def sem_colisao_horizontal(self):
        jogador = self.jogador.sprite
        jogador.colisao_direita = False
        jogador.colisao_esquerda = False

    def run(self):

        # Tiles do Level
        self.tiles.update(self.deslocamento_level_x)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        # Jogador
        self.jogador.update()
        self.sem_colisao_horizontal()
        self.colisao_movimento_vertical()
        self.colisao_movimento_horizontal()
        self.jogador.draw(self.display_surface)
