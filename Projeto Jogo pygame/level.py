import pygame
from tiles import Tile, TileEstatico
from configs import tamanho_tile, largura_display, altura_display
from dicionários import *
from jogador import Jogador
from funcoes_suporte import importar_arquivos_csv, importar_graficos

class Level:
    def __init__(self, level_data, superficie):
        self.display_surface = superficie
        self.imagem = pygame.image.load('./levels/level_1/level_1.png')
        # layout_terreno = importar_arquivos_csv(level_data['terreno'])




        self.sprites_terreno = self.setup_level(level_data,superficie)


        self.deslocamento_level_x = 0  # Movimento horizontal do level
        self.deslocamento_level_y = 0  # Movimento vertical do level


    def setup_level(self, layout,tipo):
        self.tiles = pygame.sprite.Group()
        self.jogador = pygame.sprite.GroupSingle()
        

        for index_linha, linha in enumerate(layout):
            for index_coluna, celula in enumerate(linha):
                x = index_coluna * tamanho_tile
                y = index_linha * tamanho_tile
                if celula == 'X':
                    
                    tile = Tile((x, y), tamanho_tile,'ground_2')  # Posição (x,y); Tamanho (tile_size de settings, padrão = 64)
                    self.tiles.add(tile)

                if celula == 'Y':
                    tile = Tile((x, y), tamanho_tile,
                                'ground_5')
                    self.tiles.add(tile)
                    
                if celula == 'Z':
                    tile = Tile((x, y), tamanho_tile,
                                'ground_1')
                    self.tiles.add(tile)
                if celula == 'z':
                    tile = Tile((x, y), tamanho_tile,
                                'ground_3')
                    self.tiles.add(tile)
                if celula == 'W':
                    tile = Tile((x, y), tamanho_tile,
                                'ground_4')
                    self.tiles.add(tile)
                if celula == 'w':
                    tile = Tile((x, y), tamanho_tile,
                                'ground_6')
                    self.tiles.add(tile)
                if celula == 'K':
                    tile = Tile((x, y), tamanho_tile,
                                'ground_10')
                    self.tiles.add(tile)
                if celula == 'k':
                    tile = Tile((x, y), tamanho_tile,
                                'ground_11')
                    self.tiles.add(tile)
                if celula == 'I':
                    tile = Tile((x, y), tamanho_tile,
                                'ground_7')
                    self.tiles.add(tile)
                if celula == 'i':
                    tile = Tile((x, y), tamanho_tile,
                                'ground_9')
                    self.tiles.add(tile)
                if celula == 'J':
                    tile = Tile((x, y), tamanho_tile,
                                'ground_8')
                    self.tiles.add(tile)
                
                if celula == 'P':

                    sprite_jogador = Jogador((x,y))
                    self.jogador.add(sprite_jogador)


                
                

        return self.tiles
    def scroll_x(self):
        jogador = self.jogador.sprite
        jogador_x = jogador.rect.centerx
        direcao_x = jogador.direcao.x
        keys = pygame.key.get_pressed()

        if jogador_x < largura_display / 4 and direcao_x < 0:
            self.deslocamento_level_x = jogador.velocidade_inicial
            jogador.velocidade = 0

        elif jogador_x > largura_display - (largura_display / 2) and direcao_x > 0:
            self.deslocamento_level_x = -jogador.velocidade_inicial
            jogador.velocidade = 0

        else:
            self.deslocamento_level_x = 0
            jogador.velocidade = jogador.velocidade_inicial
    def scroll_y(self):
        jogador = self.jogador.sprite
        jogador_y = jogador.rect.centery
        direcao_y = jogador.direcao.y
        keys = pygame.key.get_pressed()


        if jogador_y < altura_display / 6 and not direcao_y < 0:
            self.deslocamento_level_y = jogador.direcao.y * 2


        elif jogador_y > altura_display - (altura_display / 6):
            self.deslocamento_level_y = -6
            jogador.direcao.y = 0
        else:
            self.deslocamento_level_y = 0



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

        self.sprites_terreno.draw(self.display_surface)
        self.tiles.update(self.deslocamento_level_x,self.deslocamento_level_y)



        # self.tiles.draw(self.display_surface)

        self.scroll_x()
        self.scroll_y()

        # Jogador
        self.jogador.update()
        self.sem_colisao_horizontal()
        self.colisao_movimento_vertical()
        self.colisao_movimento_horizontal()
        self.jogador.draw(self.display_surface)

        # Inimigo






