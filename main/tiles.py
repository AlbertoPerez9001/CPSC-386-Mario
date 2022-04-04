import pygame as pg
from pygame.sprite import Sprite

class Tile(Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pg.Surface((size,size))
        self.image.fill('grey')
        self.image = pg.transform.rotozoom(pg.image.load('sprites/brick.png'),0,2)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self,xshift):
        self.rect.x += xshift

class Pipe(Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pg.Surface((size,size))
        self.image.fill('grey')
        self.image = pg.transform.rotozoom(pg.image.load('sprites/pipe.png'),0,2)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self,xshift):
        self.rect.x += xshift

class BreakBrick(Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pg.Surface((size,size))
        self.image.fill('grey')
        self.image = pg.transform.rotozoom(pg.image.load('sprites/breakbrick.png'),0,2)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self,xshift):
        self.rect.x += xshift

class Qblock(Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.size = size
        self.image = pg.Surface((self.size,self.size))
        self.image.fill('grey')
        self.image = pg.transform.rotozoom(pg.image.load('sprites/coin.png'),0,2)
        self.rect = self.image.get_rect(topleft=pos)
        self.new = True

    def hit(self):
        if self.new:
            self.new = False
            self.image = pg.Surface((self.size,self.size))
            self.image.fill('grey')
            self.image = pg.transform.rotozoom(pg.image.load('sprites/EmptyBlock.png'),0,2)
            self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def update(self,xshift):
        self.rect.x += xshift


class Warp(Sprite):
    def __init__(self, pos, size, up_or_side):
        super().__init__()
        self.up = up_or_side
        self.image = pg.Surface((size,size))
        self.image.fill('grey')
        if not self.up:
            self.image = pg.transform.rotozoom(pg.image.load('sprites/pipe.png'),90,2)
        else:
            self.image = pg.transform.rotozoom(pg.image.load('sprites/pipe.png'),0,2)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self,xshift):
        self.rect.x += xshift

class Flag(Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pg.Surface((size,size))
        self.image.fill('grey')
        self.image = pg.transform.rotozoom(pg.image.load('sprites/FlagOnCastle.png'),0,3)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self,xshift):
        self.rect.x += xshift