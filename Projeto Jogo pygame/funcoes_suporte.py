from os import walk
def importar_arquivo(caminho):
    lista_superficies = []
    for _,__,arquivos_imagem in walk(caminho):
        for imagem in arquivos_imagem:
            diretorio_completo = caminho + '/' + imagem

importar_arquivo('./sprites/player/idle')