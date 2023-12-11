import pygame, sys
from configs import *
from level import Level
from dicionários import *



# Bases para o código:
# Criação e movimento dos tiles + animações dos personagens baseados no canal Clear Code: https://www.youtube.com/watch?v=YWN8GcmJ-jA&t=6697s ; https://www.youtube.com/watch?v=wJMDh9QGRgs&t=5969s
# Assets: https://brullov.itch.io/oak-woods, https://cainos.itch.io/pixel-art-platformer-village-props, https://luizmelo.itch.io/monsters-creatures-fantasy
# Sprites do jogador: https://themessengergame.com/

class Game:
    def __init__(self):
        pygame.init()
        Titulo = "Marked by the Kage"

        self.display = pygame.display.set_mode((largura_display, altura_display))
        pygame.display.set_caption(Titulo)

        self.clock = pygame.time.Clock()
        self.level = Level(mapa_level, self.display)
        self.menu = True
        self.opcoes = 1
        self.creditos = False
        self.menu_principal = True
        self.game_over = False


        self.cont_opcoes = False
        self.cont_enter = False


        self.fonte = pygame.font.Font('./fonte/lastninja.ttf', 150)
        self.fonte2 = pygame.font.Font('./fonte/lastninja.ttf', 50)

        self.bg1 = pygame.image.load("./Graphics/background/background_layer_1.png", ).convert_alpha()
        self.bg1 = pygame.transform.scale(self.bg1, (320 * 50, 180 * 4))

        self.bg2 = pygame.image.load("./Graphics/background/background_layer_2.png").convert_alpha()
        self.bg2 = pygame.transform.scale(self.bg2, (320 * 50, 180 * 4))

        self.bg3 = pygame.image.load("./Graphics/background/background_layer_3.png").convert_alpha()
        self.bg3 = pygame.transform.scale(self.bg3, (320 * 50, 180 * 4))

        self.img_pos1 = [-320 * 25, 0]
        self.img_pos2 = [-320 * 25, 0]
        self.img_pos3 = [-320 * 25, 0]

        # self.v_movement = [False, False]
        self.level.h_movement = [False, False]

        # HUD jogador

        self.hp_3 = pygame.image.load("./sprites/HUD/hp/3 vidas.png").convert_alpha()
        self.hp_3 = pygame.transform.scale(self.hp_3, (32 * 3 * 1.25 + 20 * 1.25, 32 * 1.25))

        self.hp_2 = pygame.image.load("./sprites/HUD/hp/2 vidas.png").convert_alpha()
        self.hp_2 = pygame.transform.scale(self.hp_2, (32 * 3 * 1.25 + 20 * 1.25, 32 * 1.25))

        self.hp_1 = pygame.image.load("./sprites/HUD/hp/1 vida.png").convert_alpha()
        self.hp_1 = pygame.transform.scale(self.hp_1, (32 * 3 * 1.25 + 20 * 1.25, 32 * 1.25))

        # self.hp_0 = pygame.image.load("./sprites/HUD/hp/0 vidas.png").convert_alpha()
        # self.hp_0 = pygame.transform.scale(self.hp_1, (32 * 3 + 20, 32))

        self.moedas = pygame.image.load("./levels/tile_sets/Texture/coin.png").convert_alpha()
        self.moedas = pygame.transform.scale(self.moedas, (32, 32))

    def hud(self):
        for jogador in self.level.jogador:

            if jogador.game_over:
                self.game_over = True



            if jogador.vida < 3:
                self.hp_3 = self.hp_2

                if jogador.vida < 2:
                    self.hp_2 = self.hp_1

                    if jogador.vida < 1:
                        self.hp_3 = pygame.transform.scale(self.hp_1, (0, 0))




            self.fonte_hud = pygame.font.Font('./fonte/lastninja.ttf', 16)
            self.cont_moedas = self.fonte_hud.render(f'x{jogador.moedas}', True, 'white')



    def run(self):



        # menu_principal = pygame.Rect(0, 0, largura_display,
        #                       altura_display)
        # pygame.draw.rect(self.display, '#664BFA', menu_principal)

        while True:  # Atualização constante da tela
            # self.img_pos1[1] += (self.v_movement[1] - self.v_movement[0]) * 5
            # self.img_pos2[1] += (self.v_movement[1] - self.v_movement[0]) * 3
            # self.img_pos3[1] += (self.v_movement[1] - self.v_movement[0]) * 2

            self.img_pos1[0] += (self.level.h_movement[1] - self.level.h_movement[0]) * 1.75
            self.img_pos2[0] += (self.level.h_movement[1] - self.level.h_movement[0]) * 1.25
            self.img_pos3[0] += (self.level.h_movement[1] - self.level.h_movement[0]) * 1

            if self.menu:
                if self.creditos:
                    creditos = pygame.image.load("./Graphics/menu/creditos.png").convert()
                    self.display.blit(creditos,(0,0))

                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        self.creditos = False
                        self.menu_principal = True

                else:

                    if self.menu_principal:
                        menu_principal = pygame.image.load("./Graphics/menu/menu_principal.png").convert()
                        menu_principal = pygame.transform.scale(menu_principal, (1601, 720))
                        self.display.blit(menu_principal, (0, 0))


                    if pygame.key.get_pressed()[pygame.K_UP] and not self.cont_opcoes:
                        self.opcoes -= 1
                        self.cont_opcoes = True

                    if pygame.key.get_pressed()[pygame.K_DOWN] and not self.cont_opcoes:
                        self.opcoes += 1
                        self.cont_opcoes = True

                    elif not pygame.key.get_pressed()[pygame.K_UP] and not pygame.key.get_pressed()[pygame.K_DOWN]:
                        self.cont_opcoes = False

                    if self.opcoes > 3:
                        self.opcoes = 1

                    if self.opcoes < 1:
                        self.opcoes = 3

                    altura_retangulo = 100
                    largura_retangulo = 400


                    if self.opcoes == 1:
                        opcao1 = pygame.Rect(largura_display // 2 - largura_retangulo // 2, altura_display // 2 - 60,
                                             largura_retangulo, altura_retangulo)
                        pygame.draw.rect(self.display, '#3F56CC', opcao1)



                        opcao2 = pygame.Rect(largura_display // 2 - largura_retangulo // 2,
                                             altura_display // 2 + altura_display // 6 - 60,
                                             largura_retangulo, altura_retangulo)
                        pygame.draw.rect(self.display, '#9547E6', opcao2)

                        opcao3 = pygame.Rect(largura_display // 2 - largura_retangulo // 2,
                                             altura_display // 2 + altura_display // 3 - 60,
                                             largura_retangulo, altura_retangulo)
                        pygame.draw.rect(self.display, '#9547E6', opcao3)

                        Start = self.fonte2.render('Start', True, 'white')

                        largura_fonte_start = Start.get_width()
                        altura_fonte_start = Start.get_height()

                        self.display.blit(Start, (largura_display // 2 - largura_retangulo // 2 + (largura_retangulo // 2 - largura_fonte_start // 2),  altura_display // 2 - 60 + altura_fonte_start // 2))

                        Creditos = self.fonte2.render('Creditos', True, 'black')

                        largura_fonte_creditos = Creditos.get_width()
                        altura_fonte_creditos = Creditos.get_height()

                        self.display.blit(Creditos, (largura_display // 2 - largura_retangulo // 2 + (largura_retangulo // 2 - largura_fonte_creditos // 2),altura_display // 2 + altura_display // 6 - 60 + altura_fonte_creditos // 2))

                        Sair = self.fonte2.render('Sair', True, 'black')

                        largura_fonte_sair = Sair.get_width()
                        altura_fonte_sair = Sair.get_height()

                        self.display.blit(Sair, (largura_display // 2 - largura_retangulo // 2 + (
                                largura_retangulo // 2 - largura_fonte_sair // 2),
                                                     altura_display // 2 + altura_display // 3 - 60 + altura_fonte_sair // 2))

                    if self.opcoes == 2:
                        opcao1 = pygame.Rect(largura_display // 2 - largura_retangulo // 2, altura_display // 2 - 60,
                                             largura_retangulo, altura_retangulo)
                        pygame.draw.rect(self.display, '#9547E6', opcao1)

                        opcao2 = pygame.Rect(largura_display // 2 - largura_retangulo // 2,
                                             altura_display // 2 + altura_display // 6 - 60,
                                             largura_retangulo, altura_retangulo)
                        pygame.draw.rect(self.display, '#3F56CC', opcao2)

                        opcao3 = pygame.Rect(largura_display // 2 - largura_retangulo // 2,
                                             altura_display // 2 + altura_display // 3 - 60,
                                             largura_retangulo, altura_retangulo)
                        pygame.draw.rect(self.display, '#9547E6', opcao3)


                        Start = self.fonte2.render('Start', True, 'black')

                        largura_fonte_start = Start.get_width()
                        altura_fonte_start = Start.get_height()

                        self.display.blit(Start, (
                        largura_display // 2 - largura_retangulo // 2 + (largura_retangulo // 2 - largura_fonte_start // 2),
                        altura_display // 2 - 60 + altura_fonte_start // 2))

                        Creditos = self.fonte2.render('Creditos', True, 'white')

                        largura_fonte_creditos = Creditos.get_width()
                        altura_fonte_creditos = Creditos.get_height()

                        self.display.blit(Creditos, (largura_display // 2 - largura_retangulo // 2 + (
                                    largura_retangulo // 2 - largura_fonte_creditos // 2),
                                                     altura_display // 2 + altura_display // 6 - 60 + altura_fonte_creditos // 2))

                        Sair = self.fonte2.render('Sair', True, 'black')

                        largura_fonte_sair = Sair.get_width()
                        altura_fonte_sair = Sair.get_height()

                        self.display.blit(Sair, (largura_display // 2 - largura_retangulo // 2 + (
                                largura_retangulo // 2 - largura_fonte_sair // 2),
                                                 altura_display // 2 + altura_display // 3 - 60 + altura_fonte_sair // 2))


                    if self.opcoes == 3:
                        opcao1 = pygame.Rect(largura_display // 2 - largura_retangulo // 2, altura_display // 2 - 60,
                                             largura_retangulo, altura_retangulo)
                        pygame.draw.rect(self.display, '#9547E6', opcao1)

                        opcao2 = pygame.Rect(largura_display // 2 - largura_retangulo // 2,
                                             altura_display // 2 + altura_display // 6 - 60,
                                             largura_retangulo, altura_retangulo)
                        pygame.draw.rect(self.display, '#9547E6', opcao2)

                        opcao3 = pygame.Rect(largura_display // 2 - largura_retangulo // 2,
                                             altura_display // 2 + altura_display // 3 - 60,
                                             largura_retangulo, altura_retangulo)
                        pygame.draw.rect(self.display, '#3F56CC', opcao3)

                        Start = self.fonte2.render('Start', True, 'black')

                        largura_fonte_start = Start.get_width()
                        altura_fonte_start = Start.get_height()

                        self.display.blit(Start, (
                        largura_display // 2 - largura_retangulo // 2 + (largura_retangulo // 2 - largura_fonte_start // 2),
                        altura_display // 2 - 60 + altura_fonte_start // 2))

                        Creditos = self.fonte2.render('Creditos', True, 'black')

                        largura_fonte_creditos = Creditos.get_width()
                        altura_fonte_creditos = Creditos.get_height()

                        self.display.blit(Creditos, (largura_display // 2 - largura_retangulo // 2 + (
                                    largura_retangulo // 2 - largura_fonte_creditos // 2),
                                                     altura_display // 2 + altura_display // 6 - 60 + altura_fonte_creditos // 2))

                        Sair = self.fonte2.render('Sair', True, 'white')

                        largura_fonte_sair = Sair.get_width()
                        altura_fonte_sair = Sair.get_height()

                        self.display.blit(Sair, (largura_display // 2 - largura_retangulo // 2 + (
                                largura_retangulo // 2 - largura_fonte_sair // 2),
                                                 altura_display // 2 + altura_display // 3 - 60 + altura_fonte_sair // 2))

            # Pause

            if pygame.key.get_pressed()[pygame.K_RETURN]:  ### TESTE ###

                if self.opcoes == 1:
                    self.menu = False
                    self.menu_principal = False
                if self.opcoes == 2:
                    self.creditos = True
                if self.opcoes == 3:
                    if not self.menu_principal:
                        self.menu_principal = True
                    elif self.menu_principal and not self.cont_enter:
                        pygame.quit()
                        sys.exit()

                self.cont_enter = True

            elif not pygame.key.get_pressed()[pygame.K_RETURN]:
                self.cont_enter = False

            if pygame.key.get_pressed()[pygame.K_ESCAPE] and not self.menu and not self.game_over:
                self.menu = True

                Pause = self.fonte.render('Pause', True, 'white')
                tamanho_fonte = Pause.get_width()

                menu_principal = pygame.Surface((largura_display, altura_display))
                menu_principal.set_alpha(128)
                menu_principal.fill((30, 30, 30))
                self.display.blit(menu_principal, (0, 0))
                self.display.blit(Pause, (largura_display // 2 - tamanho_fonte // 2, altura_display * 0.125))

            if not self.menu:
                self.display.fill((30, 30, 30))
                self.display.blit(self.bg1, self.img_pos1)
                self.display.blit(self.bg2, self.img_pos2)
                self.display.blit(self.bg3, self.img_pos3)

                self.level.run()

                self.hud()

                self.display.blit(self.hp_3, (32, 32))

                self.display.blit(self.moedas, (32, 32 + 64))

                self.display.blit(self.cont_moedas, (32 + 36, 32 + 72))


                if self.game_over:
                    game_over = pygame.image.load('./Graphics/menu/game_over.png')
                    self.display.blit(game_over, (0, 0))

                    Recomecar = self.fonte2.render('Pressione R para recomecar', True, 'white')
                    largura_fonte = Recomecar.get_width()
                    altura_fonte = Recomecar.get_height()


                    self.display.blit(Recomecar, (largura_display // 2 - largura_fonte // 2,altura_display // 2 + altura_display // 3 - 60 + altura_fonte // 2))






            # RESET #
            if pygame.key.get_pressed()[pygame.K_r]:
                Game().run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)


Game().run()
