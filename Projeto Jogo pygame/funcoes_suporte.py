from os import walk
import pygame

def importar_arquivo(caminho):
    lista_superficies = []
    for _,__,arquivos_imagem in walk(caminho):
        for imagem in arquivos_imagem:
            diretorio_completo = caminho + '/' + imagem
            superficie_imagem = pygame.image.load(diretorio_completo).convert_alpha()
            lista_superficies.append(superficie_imagem)

        return lista_superficies
