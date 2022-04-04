import pygame as pg
from pygame.sprite import Sprite
from support import import_folder

class Item(Sprite):
    def __init__(self, pos, p, s):
        super().__init__()
        self.player = p
        self.state = s
        self.char_assets()
        self.frame_index = 0
        self.anime_speed = 0.05
        self.image = self.animations[self.state][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pg.Vector2(0,0)
        if self.state == 'mushroom':
            self.direction.x = 1
        else:
            self.direction.x = 0
        self.speed = 7
        self.gravity = 0.8

    def char_assets(self):
        char_path ='sprites/items/'
        self.animations = {'mushroom':[], 'fire_flower':[], 'star':[], 'coin':[]}
        for anime in self.animations.keys():
            full_path = char_path + anime
            self.animations[anime] = import_folder(full_path)

    def get_state(self):
        if self.state != 'coin': 
            if not self.player.powered:
                self.state = 'mushroom'
                self.direction.x = 1
            elif not self.player.fire:
                self.state = 'fire_flower'
                self.direction.x = 0

    def animate(self):
        animate = self.animations[self.state]

        self.frame_index += self.anime_speed
        if self.frame_index >= len(animate):
            self.frame_index = 0
        image = animate[int(self.frame_index)]
        self.image = image

    def grav(self):
        if self.state != 'coin':
            self.direction.y += self.gravity
            self.rect.y += self.direction.y

    def update(self,xshift):
        # self.get_state()
        self.animate()
        self.rect.x += xshift