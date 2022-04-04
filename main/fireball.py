import pygame as pg
from pygame.sprite import Sprite
from support import import_folder

class Fireball(Sprite):
    def __init__(self,pos,p,lor=True):
        super().__init__()
        self.player = p
        self.right = lor
        self.char_assets()
        self.frame_index = 0
        self.anime_speed = 0.05
        self.image = self.animations['fire_ball'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pg.Vector2(1,0)
        if self.right:
            self.speed = 6
        else:
            self.speed = -6
        self.state = 'fire_ball'




    def char_assets(self):
        char_path ='sprites/'
        self.animations = {'fire_ball':[]}
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

    def update(self,xshift):
        self.animate()
        self.rect.x += xshift