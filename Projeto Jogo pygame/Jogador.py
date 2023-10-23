import pygame, sys
from configs import largura_display
from funcoes_suporte import importar_arquivo

class Jogador(pygame.sprite.Sprite):  # Parametros do Jogador:
    def __init__(self, posicao):
        super().__init__()
        self.image = pygame.Surface((32, 64))  # Tamanho (w,h)
        self.image.fill('Gray')
        self.rect = self.image.get_rect(topleft=posicao)
        # Movimentação do jogador:
        self.direcao = pygame.math.Vector2(0, 0)
        self.velocidade_corrida = 15  # Velocidade máxima do personagem
        self.velocidade_inicial = 8
        self.velocidade = 10
        self.velocidade_level = self.velocidade_corrida
        self.gravidade = 0.5
        self.velocidade_pulo = -16
        self.colisao_topo = False
        self.colisao_chao = False
        self.colisao_direita = False
        self.colisao_esquerda = False
        self.agarrando_parede = False
        self.limite_pulo = 0

    def importar_sprites_personagens(self):
        diretorio = '/sprites/player'
        self.grafico_personagem =  {'idle':[],'running':[],'run_atk':[],'jumping':[],'falling':[],'duck_idle':[],'duck_atk':[],'damage':[],'gliding':[],'wall_grab':[],'wall_moving':[]}

        for graficos in self.grafico_personagem:
            self.diretorio_completo = diretorio + self.grafico_personagem
            self.grafico_personagem[graficos] = importar_arquivo(self.diretorio_completo)




    def get_input(self):  # Comandos input personagem
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direcao.x = 1




        elif keys[pygame.K_LEFT]:
            self.direcao.x = -1


        elif not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.direcao.x = 0
            self.gravidade = 0.5

        if keys[pygame.K_SPACE]:
            self.pulo()
            self.velocidade_pulo = -16

        if keys[pygame.K_x]:
            self.correr()
        if keys[pygame.K_z]:
            self.agarrar_parede()

        if keys[pygame.K_DOWN]:
            self.ground_pound()
            self.velocidade_pulo = -16

        if keys[pygame.K_ESCAPE]:  # Sair do jogo pelo 'Esc'
            pygame.quit()
            sys.exit()

    def apply_gravity(self):  # Gravidade
        self.direcao.y += self.gravidade
        self.rect.y += self.direcao.y

    def pulo(self):

        if self.colisao_chao:
            self.direcao.y = self.velocidade_pulo
        if self.direcao.y > 0:
            self.velocidade_pulo = 0
            self.direcao.y = self.velocidade_pulo

    def correr(self):

        if (self.rect.centerx < largura_display / 4 and self.direcao.x < 0) or (
                    self.rect.centerx > largura_display - (largura_display / 4) and self.direcao.x > 0):
            self.velocidade = 0
        else:
            self.velocidade = self.velocidade_corrida

    def agarrar_parede(self):
        keys = pygame.key.get_pressed()
        if not self.direcao.y < 0:
            if (self.colisao_direita and keys[pygame.K_z]) or (self.colisao_esquerda and keys[pygame.K_z]):
                self.gravidade = 0
                self.direcao.y = 0

            else:
                self.gravidade = 0.5

    def ground_pound(self):
        if self.direcao.y > 0:
            self.velocidade_pulo = 32
            self.direcao.y = self.velocidade_pulo

    def update(self):
        self.get_input()
        self.apply_gravity()
