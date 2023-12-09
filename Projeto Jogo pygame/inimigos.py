import pygame
from funcoes_suporte import importar_arquivo
from jogador import Jogador
from dicionários import *

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, posicao,tipo):
        super().__init__()
        self.importar_sprites_personagens('Goblin')
        self.index_frames = 0  # Index da imagem animada
        self.velocidade_animacao_inicial = 0.15
        self.velocidade_animacao = self.velocidade_animacao_inicial
        self.image = self.grafico_personagem['idle'][self.index_frames]

        self.tamanho_imagem = 65.625

        self.image = pygame.transform.scale(self.image, (self.tamanho_imagem, self.tamanho_imagem))
        self.rect = self.image.get_rect(topleft=posicao)
        self.status = 'idle'  # Animação Atual
        # Movimentação do inimigo:
        self.direcao = pygame.math.Vector2(0, 0)
        self.velocidade_corrida = 10  # Velocidade máxima do personagem
        self.velocidade= 3.75

        self.gravidade = 0.8

        self.olhando_direita = False
        self.atacando = False









    def importar_sprites_personagens(self, tipo):
        diretorio = f'./sprites/inimigos/{tipo}/'
        self.grafico_personagem = dicionario_inimigo1 # Dicionário

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
            self.image = pygame.transform.flip(imagem, True, False)

        if self.direcao.x == 0:
            self.status = 'idle'
            self.velocidade_animacao = self.velocidade_animacao_inicial

        elif self.direcao.x != 0:
            self.status = 'running'
            self.velocidade_animacao = 0.30

        if self.atacando:
            self.status = 'attack'
            self.velocidade_animacao = 0.375
            self.atacando = False





    def aplicar_gravidade(self):  # Gravidade

        self.direcao.y += self.gravidade
        self.rect.y += self.direcao.y

    def update(self, deslocamento_x, deslocamento_y):
        self.rect.x += deslocamento_x
        self.rect.y += deslocamento_y

        self.animacao(self.status)

        self.aplicar_gravidade()
        self.image = pygame.transform.scale(self.image, (self.tamanho_imagem, self.tamanho_imagem))


