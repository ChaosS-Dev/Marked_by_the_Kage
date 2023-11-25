import pygame, sys
from configs import largura_display
from funcoes_suporte import importar_arquivo
from dicionários import *

class Jogador(pygame.sprite.Sprite):  # Parametros do Jogador:
    def __init__(self, posicao):
        super().__init__()
        self.importar_sprites_personagens()
        self.index_frames = 0   # Index da imagem animada
        self.velocidade_animacao_inicial = 0.15
        self.velocidade_animacao = self.velocidade_animacao_inicial
        self.image = self.grafico_personagem['idle'][self.index_frames]
        self.rect = self.image.get_rect(topleft=posicao)
        self.status = 'idle'    # Animação Atual
        # Movimentação do jogador:
        self.direcao = pygame.math.Vector2(0, 0)
        self.velocidade_corrida = 10  # Velocidade máxima do personagem
        self.velocidade_inicial = 5
        self.velocidade = self.velocidade_inicial
        self.velocidade_level = self.velocidade_corrida
        self.gravidade_inicial = 0.8
        self.gravidade = self.gravidade_inicial
        self.velocidade_pulo_inicial = -14
        self.velocidade_pulo = self.velocidade_pulo_inicial
        self.colisao_topo = False
        self.colisao_chao = False
        self.colisao_direita = False
        self.colisao_esquerda = False
        self.agarrando_parede = False
        self.escalando = False
        self.limite_pulo = 0
        self.olhando_direita = True

    def importar_sprites_personagens(self):
        diretorio = './sprites/player/'
        self.grafico_personagem = dicionario_jogador # Dicionário

        for graficos in self.grafico_personagem.keys():
            self.diretorio_completo = diretorio + graficos
            self.grafico_personagem[graficos] = importar_arquivo(self.diretorio_completo)

    def animacao(self,status):
        animacao = self.grafico_personagem[status]
        # Loop da animação
        self.index_frames += self.velocidade_animacao
        if self.index_frames >= len(animacao):
            self.index_frames = 0
        imagem = animacao[int(self.index_frames)]
        if self.olhando_direita:
            self.image = imagem
        else:
            self.image = pygame.transform.flip(imagem,True,False)


        if self.olhando_direita:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        else:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)

        if self.colisao_chao and self.direcao.x == 0:
            self.status = 'idle'
            self.velocidade_animacao = self.velocidade_animacao_inicial
        elif self.colisao_chao and self.direcao.x != 0:
            self.status = 'running'
            self.velocidade_animacao = self.velocidade_animacao_inicial

        if self.colisao_chao and pygame.key.get_pressed()[pygame.K_DOWN]:

            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
            self.status = 'duck_idle'
            self.velocidade_animacao = 0.05

        if not self.colisao_chao and self.direcao.y <= 0:
            self.status = 'jumping'
            self.velocidade_animacao = self.velocidade_animacao_inicial

        if not self.colisao_chao and self.direcao.y >= 0:
            if pygame.key.get_pressed()[pygame.K_SPACE] and not pygame.key.get_pressed()[pygame.K_DOWN]:
                self.status = 'gliding'
            else:
                self.status = 'falling'
            self.velocidade_animacao = self.velocidade_animacao_inicial

        if self.agarrando_parede and self.direcao.y == 0:
            self.status = 'wall_grab'
            self.velocidade_animacao = self.velocidade_animacao_inicial

        if self.escalando and (self.colisao_direita or self.colisao_esquerda):
            self.status = 'wall_moving'
            self.velocidade_animacao = self.velocidade_animacao_inicial

        if self.colisao_topo:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def get_input(self):  # Comandos input personagem
        keys = pygame.key.get_pressed()

        if not keys[pygame.K_DOWN]:
            if keys[pygame.K_RIGHT]:
                self.direcao.x = 1
                if not self.agarrando_parede:
                    self.olhando_direita = True

            elif keys[pygame.K_LEFT]:
                self.direcao.x = -1
                if not self.agarrando_parede:
                    self.olhando_direita = False

            elif not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                self.direcao.x = 0
                self.gravidade = self.gravidade_inicial

        if keys[pygame.K_SPACE]:
            if not keys[pygame.K_DOWN]:
                self.pulo()
                self.agarrar_parede()
                self.velocidade_pulo = self.velocidade_pulo_inicial
                

        if not keys[pygame.K_SPACE]:
            not self.agarrar_parede()

        if keys[pygame.K_DOWN]:
            if not self.agarrando_parede:
                self.ground_pound()
                self.velocidade_pulo = -16
                self.direcao.x = 0

        if keys[pygame.K_ESCAPE]:  # Sair do jogo pelo 'Esc'
            pygame.quit()
            sys.exit()

    def aplicar_gravidade(self):  # Gravidade
        self.direcao.y += self.gravidade
        self.rect.y += self.direcao.y

    def pulo(self):
        if self.colisao_chao:
            self.direcao.y = self.velocidade_pulo
        if self.direcao.y > 0:  # Planar
            self.velocidade_pulo = 0
            self.direcao.y = self.velocidade_pulo


    def agarrar_parede(self):
        keys = pygame.key.get_pressed()
        if not self.direcao.y < 0:
            if keys[pygame.K_SPACE] and (self.colisao_direita or self.colisao_esquerda):
                self.agarrando_parede = True

            if not keys[pygame.K_SPACE]:
                self.agarrando_parede = False
                self.escalando = False

            if self.agarrando_parede and not keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
                self.gravidade = 0
                self.direcao.y = 0
                self.direcao.x = 0

            else:
                self.gravidade = self.gravidade_inicial

            if self.agarrando_parede:
                if keys[pygame.K_UP]:
                    self.direcao.y -= 5
                    self.escalando = True
                    self.agarrando_parede = False

                if not keys[pygame.K_UP]:
                    self.escalando = False
    def ground_pound(self):
        if not self.colisao_chao:
            self.velocidade_pulo = 32
            self.direcao.y = self.velocidade_pulo

    def update(self):
        self.get_input()
        self.animacao(self.status)
