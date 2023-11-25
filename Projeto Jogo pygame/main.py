import pygame, sys
from configs import *
from level import Level
from dicionários import *



class Game:
    def __init__(self):
        pygame.init()
        Titulo = "Ninja"
        self.display = pygame.display.set_mode((1200, 720))
        pygame.display.set_caption(Titulo)

        self.clock = pygame.time.Clock()
        self.level = Level(mapa_level, self.display)

        self.bg1 = pygame.image.load("./Graphics/background/background_layer_1.png",).convert_alpha()
        self.bg1 = pygame.transform.scale(self.bg1,(320*50,180*4))

        self.bg2 = pygame.image.load("./Graphics/background/background_layer_2.png").convert_alpha()
        self.bg2 = pygame.transform.scale(self.bg2, (320 *50, 180 * 4))

        self.bg3 = pygame.image.load("./Graphics/background/background_layer_3.png").convert_alpha()
        self.bg3 = pygame.transform.scale(self.bg3 , (320 * 50, 180 * 4))


        self.img_pos1 = [-320*25, 0]
        self.img_pos2 = [-320*25, 0]
        self.img_pos3 = [-320*25, 0]

        # self.v_movement = [False, False]
        self.h_movement = [False, False]




    def run(self):
        while True:  # Atualização constante da tela
            # self.img_pos1[1] += (self.v_movement[1] - self.v_movement[0]) * 5
            # self.img_pos2[1] += (self.v_movement[1] - self.v_movement[0]) * 3
            # self.img_pos3[1] += (self.v_movement[1] - self.v_movement[0]) * 2

            self.img_pos1[0] += (self.h_movement[1] - self.h_movement[0]) * 1.75
            self.img_pos2[0] += (self.h_movement[1] - self.h_movement[0]) * 1.25
            self.img_pos3[0] += (self.h_movement[1] - self.h_movement[0]) * 1




            self.display.fill((30, 30, 30))
            self.display.blit(self.bg1,self.img_pos1)
            self.display.blit(self.bg2,self.img_pos2)
            self.display.blit(self.bg3,self.img_pos3)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.h_movement[0] = True
                    if event.key == pygame.K_LEFT:
                        self.h_movement[1] = True



                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.h_movement[0] = False
                    if event.key == pygame.K_LEFT:
                        self.h_movement[1] = False


            self.level.run()
            pygame.display.update()
            self.clock.tick(60)

Game().run()
while True:  # Atualização constante da tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
