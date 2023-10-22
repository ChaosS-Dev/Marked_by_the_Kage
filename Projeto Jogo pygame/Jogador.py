import pygame,sys
class Jogador(pygame.sprite.Sprite):            # Parametros do Player:
    def __init__(self, posicao):
        super().__init__()
        self.image = pygame.Surface((32,64))   # Tamanho (w,h)
        self.image.fill('Gray')
        self.rect = self.image.get_rect(center=posicao)
        # Movimentação do jogador:
        self.direcao = pygame.math.Vector2(0, 0)
        self.velocidade = 8
        self.gravidade = 0.8
        self.velocidade_pulo = -16
        self.colisao_topo = False
        self.colisao_chao = False
        self.limite_pulo = 0

    def get_input(self):                # Comandos input personagem
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direcao.x = 1
        elif keys[pygame.K_LEFT]:
            self.direcao.x = -1
        elif not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.direcao.x = 0

        if keys[pygame.K_SPACE] or keys[pygame.K_z]:
            self.pulo()
            self.velocidade_pulo = -16

        if keys[pygame.K_DOWN]:
            self.ground_pound()
            self.velocidade_pulo = -16





        if keys[pygame.K_ESCAPE]:   # Sair do jogo pelo 'Esc'
            pygame.quit()
            sys.exit()


    def apply_gravity(self):              # Gravidade
        self.direcao.y += self.gravidade
        self.rect.y += self.direcao.y

    def pulo(self):
        keys = pygame.key.get_pressed()

        if self.direcao.y == 0 and self.colisao_chao:
            self.direcao.y = self.velocidade_pulo
        if self.direcao.y > 0:
            self.velocidade_pulo = 0
            self.direcao.y = self.velocidade_pulo


    def ground_pound(self):
        if self.direcao.y > 0:
            self.velocidade_pulo = 32
            self.direcao.y = self.velocidade_pulo


    def update(self):
        self.get_input()
        self.apply_gravity()
