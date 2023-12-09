import pygame, sys
import time
from tiles import Tile, Obj
from configs import tamanho_tile, largura_display, altura_display
from dicionários import *
from jogador import Jogador
from inimigos import Inimigo
class Level:
    def __init__(self, level_data, superficie):
        self.display_surface = superficie

        # layout_terreno = importar_arquivos_csv(level_data['terreno'])

        self.cx = 0


        self.sprites_terreno = self.setup_level(level_data,superficie)


        self.deslocamento_level_x = 0  # Movimento horizontal do level
        self.deslocamento_level_y = 0  # Movimento vertical do level

        self.h_movement = [False, False]




    def setup_level(self, layout, tipo):
        self.baus = pygame.sprite.Group()
        self.moedas = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()

        self.final = pygame.sprite.Group()

        self.inimigo = Inimigo
        self.inimigos = pygame.sprite.Group()

        self.jogador = pygame.sprite.GroupSingle()




        for index_linha, linha in enumerate(layout):
            for index_coluna, celula in enumerate(linha):
                x = index_coluna * tamanho_tile
                y = index_linha * tamanho_tile

                # Terreno
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

                # Player
                if celula == 'P':

                    sprite_jogador = Jogador((x,y))
                    self.jogador.add(sprite_jogador)

                # Baú



                if celula == 'C':
                    bau = Obj((x, y), tamanho_tile,
                                'chest')
                    self.baus.add(bau)

                # Moeda

                if celula == 'M':
                    moeda = Obj((x, y), tamanho_tile,
                               'coin')
                    self.moedas.add(moeda)

                # Inimigos
                x = index_coluna * tamanho_tile
                y = index_linha * (tamanho_tile-10)
                if celula == '1':
                    sprite_inimigo1 = Inimigo((x, y),'1')
                    self.inimigos.add(sprite_inimigo1)




                if celula == 'T':
                    tile = Tile((x, y), tamanho_tile,
                                'blank')
                    self.tiles.add(tile)

                if celula == 'F':
                    final = Obj((x, y+3*tamanho_tile+13), tamanho_tile,
                              'vazio')
                    self.final.add(final)


                
                

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


        if jogador_y < altura_display / 5 and not direcao_y < 0:
            if jogador.status != 'gliding':
                self.deslocamento_level_y = 6
            if jogador.status == 'gliding':
                self.deslocamento_level_y = 3

        elif jogador_y > altura_display - (altura_display / 5):
            if jogador.status != 'gliding':
                self.deslocamento_level_y = -6
            if jogador.status == 'gliding':
                self.deslocamento_level_y = -3
            jogador.direcao.y = 0
        else:
            self.deslocamento_level_y = 0



    def colisao_movimento_horizontal(self):  # Colisões laterais com os tiles
        jogador = self.jogador.sprite
        jogador.rect.x += jogador.direcao.x * jogador.velocidade
        tolerancia_colisao = 50

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(jogador.rect):  # Colisão de parede com jogador
                if jogador.direcao.x < 0 and abs(jogador.rect.left - tile.rect.right) < tolerancia_colisao:
                    jogador.rect.left = tile.rect.right
                    jogador.colisao_esquerda = True
                    jogador.direcao.x = 0


                elif jogador.direcao.x > 0 and abs(jogador.rect.right - tile.rect.left) < tolerancia_colisao:
                    jogador.rect.right = tile.rect.left
                    jogador.colisao_direita = True
                    jogador.direcao.x = 0

                for inimigo in self.inimigos.sprites():
                    if inimigo.rect.colliderect(tile):
                        if inimigo.direcao.x > 0 and abs(inimigo.rect.right - tile.rect.left) < tolerancia_colisao:
                            inimigo.rect.right = tile.rect.left
                            inimigo.direcao.x = 0

                        if inimigo.rect.colliderect(tile):
                            if inimigo.direcao.x < 0 and abs(inimigo.rect.left - tile.rect.right) < tolerancia_colisao:
                                inimigo.rect.left = tile.rect.right
                                inimigo.direcao.x = 0


    def colisao_movimento_vertical(self):
        jogador = self.jogador.sprite
        inimigos = self.inimigos.sprites
        tolerancia_colisao = 50
        jogador.aplicar_gravidade()
        for tile in self.tiles.sprites():
            if tile.rect.colliderect(jogador.rect):  # Colisão de parede com jogador
                if jogador.direcao.y > 0 and abs(jogador.rect.bottom - tile.rect.top) < tolerancia_colisao:
                    jogador.rect.bottom = tile.rect.top
                    jogador.direcao.y = 0
                    jogador.colisao_chao = True
                    jogador.colisao_inimigo = False


                elif jogador.direcao.y < 0 and abs(jogador.rect.top - tile.rect.bottom) < tolerancia_colisao:
                    jogador.rect.top = tile.rect.bottom
                    jogador.direcao.y = 0
                    jogador.colisao_topo = True

            for inimigo in self.inimigos.sprites():
                if inimigo.rect.colliderect(tile):
                    if inimigo.direcao.y > 0 and abs(inimigo.rect.bottom - tile.rect.top) < tolerancia_colisao:
                        inimigo.rect.bottom = tile.rect.top
                        inimigo.direcao.y = 0



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



    def coletar_moedas(self):
        jogador = self.jogador.sprite
        for coin in self.moedas:
            if coin.rect.colliderect(jogador.rect):
                # coin.kill()
                self.moedas.remove(coin)
                jogador.moedas+=1


    def coletar_baus(self):
        jogador = self.jogador.sprite
        for bau in self.baus:
            if bau.rect.colliderect(jogador.rect):
                self.baus.remove(bau)
                jogador.moedas += 10


    def final_creditos(self):
        jogador = self.jogador.sprite
        for final in self.final:
            if final.rect.colliderect(jogador.rect):
                pygame.quit()
                sys.exit()



    def interacao_inimigo_jogador(self):
        jogador = self.jogador.sprite


        for inimigo in self.inimigos.sprites():

            if jogador.rect.colliderect(inimigo): # Colisão com inimigo
                inimigo.atacando = True
                jogador.colisao_inimigo = True

            if jogador.colisao_inimigo:

                if not jogador.colidiu_inimigo:
                    jogador.direcao.y = -10
                    jogador.colidiu_inimigo = True

                if inimigo.olhando_direita:
                    jogador.direcao.x = 1
                else:
                    jogador.direcao.x = -1

            else:
                inimigo.direcao.x = 0

            if not inimigo.status == 'attack':
                if not jogador.colisao_inimigo:
                    jogador.colidiu_inimigo = False

                    if abs(jogador.rect.y - inimigo.rect.y) < inimigo.tamanho_imagem + 5:

                        if 25 < jogador.rect.x - inimigo.rect.x < 375:
                            inimigo.direcao.x = 1

                        if -25 > jogador.rect.x - inimigo.rect.x > -375:
                            inimigo.direcao.x = -1

                    else:
                        inimigo.direcao.x = 0





            if inimigo.direcao.x > 0:
                inimigo.olhando_direita = True

            if inimigo.direcao.x < 0:
                inimigo.olhando_direita = False


            if inimigo.direcao.x != 0:
                inimigo.rect.x += inimigo.direcao.x * inimigo.velocidade






    def background(self):

            if self.deslocamento_level_x < 0:
                self.h_movement[0] = True
            elif self.deslocamento_level_x > 0:
                self.h_movement[1] = True
            else:
                self.h_movement = [False, False]




    def run(self):

        # Tiles do Level

        self.sprites_terreno.draw(self.display_surface)
        self.tiles.update(self.deslocamento_level_x,self.deslocamento_level_y)
        self.moedas.update(self.deslocamento_level_x, self.deslocamento_level_y)
        self.baus.update(self.deslocamento_level_x, self.deslocamento_level_y)
        self.final.update(self.deslocamento_level_x, self.deslocamento_level_y)

        # self.tiles.draw(self.display_surface)

        self.scroll_x()
        self.scroll_y()

        # Jogador
        self.jogador.update()
        self.sem_colisao_horizontal()
        self.colisao_movimento_vertical()
        self.colisao_movimento_horizontal()
        self.coletar_moedas()
        self.coletar_baus()

        self.moedas.draw(self.display_surface)
        self.baus.draw(self.display_surface)

        self.jogador.draw(self.display_surface)
        self.final.draw(self.display_surface)

        # Inimigos
        self.inimigos.update(self.deslocamento_level_x, self.deslocamento_level_y)
        self.inimigos.draw(self.display_surface)
        self.interacao_inimigo_jogador()


        # Background

        self.background()

        self.final_creditos()






