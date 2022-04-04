
class Settings:
    level_map = [
        '                                                                                                                                             ',
        '                                                                                                                                             ',
        '                                                                                                                                             ',
        '                   Q                                                                       G     G  G                                        ',
        '   P                                                                                     BBBBBBBBBBB        BBBBBQ                           ',
        '                   F                                                                                                                         ',
        '            Q    BQBQB        M                                                     BQB                         B                            ',
        '                              T               W                 T                                                     W                      ',
        '               G    G  M              G               G  G                        G                                                          ',
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXX                      ',
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXX                      ',]

    underground_map = [
        'X P XXXXXXXXXXXXXXXXXXX ',
        'X                       ',
        'X                       ',
        'X                       ',
        'X        CCCCCC         ',
        'X       CCCCCCCC        ',
        'X       CCCCCCCC        ',
        'X       XXXXXXXX      W  ',
        'X       XXXXXXXX        ',
        'XXXXXXXXXXXXXXXXXXXXXXXX',
        'XXXXXXXXXXXXXXXXXXXXXXXX',]

    end_map = [
        '                                   ',
        '                                   ',
        '                                   ',
        '                                   ',
        '                          X        ',
        '                         XX        ',
        ' P      BBBBQB          XXX        ',
        ' T                T    XXXX        ',
        '                G     XXXXX    H   ',
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',]

    tile_size = 64
    screen_width = 1200
    screen_height = len(level_map)*tile_size

    player_lives = 5
    player_coins = 0

    powered = False
    fire = False