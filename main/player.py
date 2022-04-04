import pygame as pg
from pygame.sprite import Sprite, Group
from fireball import Fireball
from support import import_folder

class Player(Sprite):
    def __init__(self, pos, game):
        super().__init__()
        self.game = game
        self.char_asset()
        self.frame_index = 0
        self.anime_speed = 0.05
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pg.Vector2(0,0)
        self.fballs = Group()
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -18
        self.state = 'idle'
        self.powered = self.game.settings.powered
        self.fire = self.game.settings.fire
        self.faceR = True
        self.grounded = False
        self.roofed = False
        self.left_walled = False
        self.right_walled =False
        self.crouch = False
        self.dead = False

    def char_asset(self):
        char_path = 'sprites/'
        self.animations = {'idle':[], 'run':[], 'jump':[], 'super_idle':[], 'super_run':[], 'super_jump':[], 'super_duck':[], 'fire_idle':[], 'fire_run':[], 'fire_jump':[], 'fire_duck':[]}

        for anime in self.animations.keys():
            full_path = char_path + anime
            self.animations[anime] = import_folder(full_path)

    def fire_ball(self):
        if self.faceR:
            fball = Fireball(self.rect.midright, p=self, lor=True)
        else:
            fball = Fireball(self.rect.midleft, p=self, lor=False)
        self.fballs.add(fball)

    def power_up(self):
        if not self.powered:
            self.powered = True
            self.game.settings.powered = self.powered
        elif not self.fire:
            self.fire = True
            self.game.settings.fire = self.fire

    def power_down(self):
        if self.fire:
            self.fire = False
            self.game.settings.fire = self.fire
        elif self.powered:
            self.powered = False
            self.game.settings.powered = self.powered


    def hit(self):
        if self.powered or self.fire:
            self.power_down()
            self.game.sound.play_pow_down()
        else:
            self.dead = True

    def get_state(self):
        if self.direction.y < 0:
            if self.fire:
                self.state = 'fire_jump'
            elif self.powered:
                self.state = 'super_jump'
            else:
                self.state = 'jump'
        elif self.direction.y > 1:
            if self.fire:
                self.state = 'fire_jump'
            elif self.powered:
                self.state = 'super_jump'
            else:
                self.state = 'jump'
        else:
            if self.direction.x != 0:
                if self.fire:
                    self.state = 'fire_run'
                elif self.powered:
                    self.state = 'super_run'
                else:
                    self.state = 'run'
            else:
                if self.crouch:
                    if self.fire:
                        self.state = 'fire_duck'
                    elif self.powered:
                        self.state = 'super_duck'
                else:
                    if self.fire:
                        self.state = 'fire_idle'
                    elif self.powered:
                        self.state = 'super_idle'
                    else:
                        self.state = 'idle'

    def animate(self):
        animate = self.animations[self.state]

        self.frame_index += self.anime_speed
        if self.frame_index >= len(animate):
            self.frame_index = 0
        image = animate[int(self.frame_index)]
        if self.faceR:
            self.image = image
        else:
            flip_img = pg.transform.flip(image,True,False)
            self.image = flip_img

        if self.grounded and self.right_walled:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.grounded and self.left_walled:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.grounded:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.roofed and self.right_walled:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.roofed and self.left_walled:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.roofed:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center = self.rect.center)

    def grav(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        if self.rect.centery > self.game.screen_height:
            self.dead = True
    

    def jump(self):
        if self.grounded:
            self.direction.y = self.jump_speed
            self.game.sound.play_jump()
            
    def update(self):
        self.get_state()
        self.animate()
