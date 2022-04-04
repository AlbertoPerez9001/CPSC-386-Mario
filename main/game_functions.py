import sys
import pygame as pg

LEFT, RIGHT, UP, DOWN, STOP, SPACE = 'left', 'right', 'up', 'down', 'stop', 'space'


dir_keys = {pg.K_LEFT: LEFT, pg.K_a: LEFT,
            pg.K_RIGHT: RIGHT, pg.K_d: RIGHT,
            pg.K_UP: UP, pg.K_w: UP,
            pg.K_DOWN: DOWN, pg.K_s: DOWN,
            pg.K_SPACE: SPACE}

def check_events(game):
    p = game.level.player.sprite
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif e.type == pg.KEYDOWN:
            if e.key in dir_keys:
                if dir_keys[e.key] == RIGHT:
                    p.direction.x = 1
                    p.faceR = True
                elif dir_keys[e.key] == LEFT:
                    p.direction.x = -1
                    p.faceR = False
                elif dir_keys[e.key] == UP:
                    p.jump()
                elif dir_keys[e.key] == DOWN:
                    p.crouch = True
                elif dir_keys[e.key] == SPACE:
                    if p.fire:
                        p.fire_ball()
                    else:
                        p.jump()
        elif e.type == pg.KEYUP:
            if e.key in dir_keys:
                if dir_keys[e.key] == RIGHT:
                    p.direction.x = 0
                elif dir_keys[e.key] == LEFT:
                    p.direction.x = 0
                elif dir_keys[e.key] == UP:
                    p.direction.y = 0
                elif dir_keys[e.key] == DOWN:
                    p.crouch = False