

dicionario_jogador = {'idle':[], 'running':[], 'run_atk':[], 'jumping':[], 'falling':[], 'duck_idle':[],
                                       'duck_atk':[], 'damage':[], 'gliding':[], 'wall_grab':[], 'wall_moving':[]}



dicionario_inimigo1 = {'idle':[], 'running':[], 'attack':[], 'jumping':[], 'falling':[], 'duck_idle':[],
                                       'duck_atk':[], 'damage':[], 'gliding':[], 'wall_grab':[], 'wall_moving':[]}






level_teste =['                              ',
             '                X              ',
             '     P          X              ',
             '    XX          X              ',
             '    XX          X              ',
             '                X              ',
             '            XX  X              ',
             '                XXXX           ',
             '              XXXXXXX          ',
             'XXXXX  XX  XXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
             '                               '
              ]

level_teste01 =[
'                                                                                                                            ZXXz                           ',
'                                                                                                                            WYYw                           ',
'                                                               ZXXXXXXXXXXXXXXXXXXXXXz                                      IJJi    ZXXz                   ',
'                                                               IJJJJJJJJJJJJJJJJJJJYYw                                              WYYYz                  ',
'                                                                                   WYw                                              WYYYYz                 ',
'                                                                                   WYw               ZXXXXXXXXXXXXXXXXXXz           IJJJJJz                ',
'                                                             ZXXXXXXXXXXXXXXXXz    WYw               IJJJJJJJJJJJJJJJJJJi                                  ',
'                                                             WYYYYYYYYYYYYYYYYw    WYw                                                                     ',
'                                                             IJJJJJJJJJJJJJJJJi    WYw                                                                     ',
'                                                                                   WYw                                                                     ',
'                                                                                   WYw                                                                     ',
'                                                                    ZXXXXXXXXXXXXXXYYw                                                                     ',
'                                                                    WYYYJJJJJJJJJJJJJi                                                                     ',
'                                                               K    IJJi                                                                                   ',
'                                                               k                                                                                           ',
'                                                                                                                        G                                 ',
' P                                    Zz                ZXz                                           ZXXXXXXXXXXXXXXXXXXXz                                ',
'ZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXz    ZYYz    ZXXXXXz    WYw                                           WYYYYYYYYYYYYYYYYYYYw                                ',
'IJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJi    IJJi    IJJJJJi    IJi                                           IJJJJJJJJJJJJJJJJJJJi                                '
    ]



level_01 =[
'                                                                                                                                                                                   ZXXz                                                                                                                                           ',
'                                                                     1       1                                                                                                     WYYw     MM                                                                                                                                    ',
'                                                               ZXXXXXXXXXXXXXXXXXXXXXz                                                                                             IJJi    ZXXz                                                                                                                                   ',
'                                                               IJJJJJJJJJJJJJJJJJJJYYYz                                                                                                    WYYYz              MM  MMM  MMMM M  MMM   MMM  MM    MM     MMM   MM  MMM        M  MM   MMM   MMM  MMMM  M M M     FFF                ',
'                                                                                   WYYYz                                                               MMMM     MMMM  1  MMMM              WYYYYz            M  M M  M M  M M M     M   M M  M M  M    M  M M  M M  M       M M  M M     M   M M  M  M M M     FFF                ',
'                                                               MMMM    MMMM        WYYYYz                                                            ZXXXXXXXXXXXXXXXXXXXXXXXXXz           WYYYYYz           M  M MMM  MMM  M M  MM MMMMM M  M M  M    MMM  M  M MMM        M M  M M  MM MMMMM MMM   M M M     FFF                ',
'                                                         ZXXXXXXXXXXXXXXXXXXXXz    WYYYYYz                                                 K         IJJJJJJJJJJJJJJJJJJJJJJJJJi           WYYYYYYz          M  M M  M M  M M M   M M   M M  M M  M    M    M  M M  M    M  M M  M M   M M   M M  M            FFF                ',
'                                                         WYYYYYYYYYYYYYYYYYYYYw    WYYYYYYz                                                k                                               WYYYYYYYz          MM  MMM  M  M M  MMM  M   M MMM   MM     M     MM  M  M     MM   MM   MMM  M   M M  M  M M M     FFF                ',
'                                                         IJJJJJJJJJJJJJJJJJJJJi    WYYYYYYYz                                                     K                                         WYYYYYYYYz                                                                                                          FFF                ',
'                                                                                   WYYYYYYYYz                                         K          k                                         WYYYYYYYYYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXz               ',
'                                                                        MMM        WYYYYYYYYYz                                        k                                                    IJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJi               ',
'                                                                    ZXXXXXXXXXXXXXXYYYYYYYYYYYz                                            K                                                                                                                                                ',
'                                                                    WYYYJJJJJJJJJJJJJJJJJJJJJJJz                                           k                                                                                                                                                ',
'                                                               K    IJJi                                                               K                                                                                                                                                    ',
'                                                               k                                    ZXXXXXXz                           k                                                                                                                                                    ',
'                                                                                                    IJJJJJJi       C    C    C    C                                                                                                                                                         ',
' P   MMM   1    C         MMM         Zz       MMM      ZXz                                                     ZXXXXXXXXXXXXXXXXXXXXXXXXXXXz                                                                                                                                               ',
'ZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXz    ZYYz    ZXXXXXz    WYw                                                     WYYYYYYYYYYYYYYYYYYYYYYYYYYYw                                                                                                                                               ',
'IJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJi    IJJi    IJJJJJi    IJi                                                     IJJJJJJJJJJJJJJJJJJJJJJJJJJJi                                                                                                                                               '
    ]






# level_1 = { 'jogador':'./levels/level_1/level_1._jogador.csv',
#          'terreno': './levels/level_1/level_1._terreno.csv',
#          'coletaveis': './levels/level_1/level_1._coletaveis.csv',
#          'decoracao01': './levels/level_1/level_1._decoracao01.csv',
#          'decoracao02': './levels/level_1/level_1._decoracao02.csv'
# }

mapa_level = level_01