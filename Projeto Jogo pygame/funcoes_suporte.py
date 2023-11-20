from os import walk
import pygame
from csv import reader
from configs import tamanho_tile
def importar_arquivo(caminho):
    lista_superficies = []
    for _,__,arquivos_imagem in walk(caminho):
        for imagem in arquivos_imagem:
            diretorio_completo = caminho + '/' + imagem
            superficie_imagem = pygame.image.load(diretorio_completo).convert_alpha()
            lista_superficies.append(superficie_imagem)

        return lista_superficies

def importar_arquivos_csv(caminho):
    with open(caminho) as mapa:
        mapa_terreno = []
        level = reader(mapa,delimiter = ',')
        for linha in level:
            mapa_terreno.append(list(linha))
        return mapa_terreno
def importar_graficos(caminho):
    superficie = pygame.image.load(caminho).convert_alpha()
    # superficie = pygame.transform.scale(superficie, (1,1))
    num_tile_x = int(superficie.get_size()[0] / tamanho_tile)
    num_tile_y = int(superficie.get_size()[1] / tamanho_tile)

    grafico_tiles = []

    for linha in range(num_tile_y):
        for coluna in range(num_tile_x):
            x = coluna * tamanho_tile
            y = linha * tamanho_tile
            nova_superficie = pygame.Surface((tamanho_tile,tamanho_tile))
            nova_superficie.blit(superficie,(0,0),pygame.Rect(x,y,tamanho_tile,tamanho_tile))
            grafico_tiles.append((nova_superficie))

    return grafico_tiles