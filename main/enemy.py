import pygame as pg
from pygame.sprite import Sprite
from support import import_folder

class Enemy(Sprite):
    def __init__(self, pos, p, s):
        super().__init__()
        self.player = p
        self.state = s
        self.char_assets()
        self.frame_index = 0
        self.anime_speed = 0.05
        self.image = self.animations[self.state][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pg.Vector2(-1,0)
        self.speed = 3
        self.gravity = 0.8
        

    def char_assets(self):
        char_path ='sprites/enemy/'
        self.animations = {'goomba':[]}
        for anime in self.animations.keys():
            full_path = char_path + anime
            self.animations[anime] = import_folder(full_path)

    def animate(self):
        animate = self.animations[self.state]

        self.frame_index += self.anime_speed
        if self.frame_index >= len(animate):
            self.frame_index = 0
        image = animate[int(self.frame_index)]
        self.image = image

    def grav(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self,xshift):
        self.animate()
        self.rect.x += xshift