import pygame as pg
from pygame.sprite import Group, GroupSingle
from enemy import Enemy
from item import Item
from player import Player
from tiles import Flag, Tile, Pipe, Qblock, BreakBrick, Warp
from time import sleep


class Level():
    def __init__(self,level_data,screen,game):
        self.game = game
        self.settings = self.game.settings
        self.display = screen
        self.level = level_data
        self.day = True
        self.setup_level(self.level)
        self.world_shift = 0
        self.current_x = 0

    def setup_level(self,layout):
        self.tiles = Group()
        self.warps = Group()
        self.blocks = Group()
        self.qblocks = Group()
        self.items = Group()
        self.enemies = Group()
        self.player = GroupSingle()
        self.goal = GroupSingle()

        for ri,r in enumerate(layout):
            for ci,c in enumerate(r):
                x = ci * self.settings.tile_size
                y = ri * self.settings.tile_size
                if c == 'X':
                    tile = Tile((x,y),self.settings.tile_size)
                    self.tiles.add(tile)
                if c == 'P': 
                    if self.player.__len__() == 0:
                        players = Player((x,y), game=self.game)
                        self.player.add(players)
                if c == 'M':
                    player = self.player.sprite
                    item = Item((x,y), player, 'mushroom')
                    self.items.add(item)
                if c == 'F':
                    player = self.player.sprite
                    item = Item((x,y), player, 'fire_flower')
                    self.items.add(item)
                if c == 'C':
                    player = self.player.sprite
                    item = Item((x,y), player, 'coin')
                    self.items.add(item)
                if c == 'G':
                    entype = 'goomba'
                    player = self.player.sprite
                    enemy = Enemy((x,y), player, entype)
                    self.enemies.add(enemy)
                if c == 'T':
                    pipe = Pipe((x,y), self.settings.tile_size)
                    self.tiles.add(pipe)
                if c == 'W':
                    wpipe = Warp((x,y), self.settings.tile_size, self.day)
                    self.warps.add(wpipe)
                if c == 'Q':
                    qb = Qblock((x, y), self.settings.tile_size)
                    self.qblocks.add(qb)
                if c == 'B':
                    breakbrick = BreakBrick((x, y), self.settings.tile_size)
                    self.blocks.add(breakbrick)
                if c == 'H':
                    flag = Flag((x,y), self.settings.tile_size)
                    self.goal.add(flag)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x > self.game.screen_width * 0.5 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        elif player_x < self.game.screen_width * 0.01 and direction_x < 0:
            self.world_shift = 0
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_collision(self):
        p = self.player.sprite
        p.rect.x += p.direction.x * p.speed
        fireb = p.fballs

        for f in fireb.sprites():
            f.rect.x += f.direction.x * f.speed
            for s in self.tiles.sprites():
                if s.rect.colliderect(f):
                    f.kill()

        for e in self.enemies.sprites():
            e.rect.x += e.direction.x * e.speed
            for s in self.tiles.sprites():
                if s.rect.colliderect(e):
                    if e.direction.x < 0:
                        e.rect.left = s.rect.right
                        e.direction.x *= -1
                    elif e.direction.x > 0:
                        e.rect.right = s.rect.left
                        e.direction.x *= -1
            for w in self.warps.sprites():
                if w.rect.colliderect(e):
                    if e.direction.x < 0:
                        e.rect.left = w.rect.right
                        e.direction.x *= -1
                    elif e.direction.x > 0:
                        e.rect.right = w.rect.left
                        e.direction.x *= -1

        for i in self.items.sprites():
            if i.state == 'mushroom':
                i.rect.x += i.direction.x * i.speed
                for s in self.tiles.sprites():
                    if s.rect.colliderect(i):
                        if i.direction.x < 0:
                            i.rect.left = s.rect.right
                            i.direction.x *= -1
                        elif i.direction.x > 0:
                            i.rect.right = s.rect.left
                            i.direction.x *= -1
                for w in self.warps.sprites():
                    if w.rect.colliderect(i):
                        if i.direction.x < 0:
                            i.rect.left = w.rect.right
                            i.direction.x *= -1
                        elif i.direction.x > 0:
                            i.rect.right = w.rect.left
                            i.direction.x *= -1

        for s in self.tiles.sprites():
            if s.rect.colliderect(p):
                if p.direction.x < 0:
                    p.rect.left = s.rect.right
                    p.left_walled = True
                    self.current_x = p.rect.left
                elif p.direction.x > 0:
                    p.rect.right = s.rect.left
                    p.right_walled = True
                    self.current_x = p.rect.right
        
        for b in self.blocks.sprites():
            if b.rect.colliderect(p):
                if p.direction.x < 0:
                    p.rect.left = b.rect.right
                    p.left_walled = True
                    self.current_x = p.rect.left
                elif p.direction.x > 0:
                    p.rect.right = b.rect.left
                    p.right_walled = True
                    self.current_x = p.rect.right
        
        for q in self.qblocks.sprites():
            if q.rect.colliderect(p):
                if p.direction.x < 0:
                    p.rect.left = q.rect.right
                    p.left_walled = True
                    self.current_x = p.rect.left
                elif p.direction.x > 0:
                    p.rect.right = q.rect.left
                    p.right_walled = True
                    self.current_x = p.rect.right

        for w in self.warps.sprites():
            if w.rect.colliderect(p):
                if p.direction.x < 0:
                    p.rect.left = w.rect.right
                    p.left_walled = True
                    self.current_x = p.rect.left
                    if not w.up:
                        self.warp()
                elif p.direction.x > 0:
                    p.rect.right = w.rect.left
                    p.right_walled = True
                    self.current_x = p.rect.right
                    if not w.up:
                        self.warp()

        if p.left_walled and (p.rect.left < self.current_x or p.direction.x >= 0):
            p.left_walled = False
        
        if p.right_walled and (p.rect.right > self.current_x or p.direction.x <= 0):
            p.right_walled = False                

    def vertical_collision(self):
        p = self.player.sprite
        p.grav()
        if p.dead:
            self.restart()
        for b in self.blocks.sprites():
            if b.rect.colliderect(p):
                if p.direction.y > 0:
                    p.rect.bottom = b.rect.top
                    p.direction.y = 0
                    p.grounded = True
                elif p.direction.y < 0:
                    p.rect.top = b.rect.bottom
                    if p.powered or p.fire:
                        b.kill()
                        self.game.sound.play_break()
                    p.direction.y = 0
                    p.roofed = True

        for q in self.qblocks.sprites():
            if q.rect.colliderect(p):
                if p.direction.y > 0:
                    p.rect.bottom = q.rect.top
                    p.direction.y = 0
                    p.grounded = True
                elif p.direction.y < 0:
                    p.rect.top = q.rect.bottom
                    if q.new:
                        self.settings.player_coins += 1
                        self.game.sound.play_coin()
                    q.hit()
                    p.direction.y = 0
                    p.roofed = True

        for s in self.tiles.sprites():
            if s.rect.colliderect(p):
                if p.direction.y > 0:
                    p.rect.bottom = s.rect.top
                    p.direction.y = 0
                    p.grounded = True
                elif p.direction.y < 0:
                    p.rect.top = s.rect.bottom
                    p.direction.y = 0
                    p.roofed = True

        for w in self.warps.sprites():
            if w.rect.colliderect(p):
                if p.direction.y > 0:
                    p.rect.bottom = w.rect.top
                    p.direction.y = 0
                    p.grounded = True
                    if w.up:
                        self.warp()
                elif p.direction.y < 0:
                    p.rect.top = w.rect.bottom
                    p.direction.y = 0
                    p.roofed = True
                    if w.up:
                        self.warp()

        for i in self.items.sprites():
            i.grav()
            for s in self.tiles.sprites():
                if i.rect.colliderect(s):
                    if i.direction.y > 0:
                        i.rect.bottom = s.rect.top
                        i.direction.y = 0
            for b in self.blocks.sprites():
                if i.rect.colliderect(b):
                    if i.direction.y > 0:
                        i.rect.bottom = b.rect.top
                        i.direction.y = 0

        if p.grounded == True and (p.direction.y < 0 or p.direction.y > 1):
            p.grounded = False

        if p.roofed == True and p.direction.y > 0:
            p.roofed = False

    def item_collision(self):
        p = self.player.sprite

        for i in self.items.sprites():
            if i.rect.colliderect(p):
                if i.state == 'mushroom':
                    if p.powered == False:
                        p.power_up()
                        self.game.sound.play_pow_up()
                    i.kill()
                elif i.state == 'fire_flower':
                    if p.fire == False:
                        p.power_up()
                        p.power_up()
                        self.game.sound.play_pow_up()
                    i.kill()
                elif i.state == 'coin':
                    self.game.sound.play_coin()
                    self.settings.player_coins += 1
                    i.kill()

    def enemy_collision(self):
        p = self.player.sprite
        fireb = p.fballs

        for f in fireb.sprites():
            for e in self.enemies.sprites():
                if e.rect.colliderect(f):
                    f.kill()
                    e.kill()

        for e in self.enemies.sprites():
            if e.rect.colliderect(p):
                if p.direction.y > 0:
                    e.kill()
                else:
                    p.hit()
                    if p.dead:
                        self.restart()
            e.grav()
            for s in self.tiles.sprites():
                if s.rect.colliderect(e):
                    if e.direction.y > 0:
                        e.rect.bottom = s.rect.top
                        e.direction.y = 0

    def goal_collision(self):
        g = self.goal.sprite
        p = self.player.sprite
        if g.rect.colliderect(p):
            self.game.sound.play_end_level()
            self.restart()

    def empty_level(self):
        self.tiles.empty()
        self.blocks.empty()
        self.qblocks.empty()
        self.items.empty()
        self.enemies.empty()
        self.player.empty()
        self.game.screen.fill(self.game.BLACK)

    def warp(self):
        self.game.sound.play_warp()
        if self.day:
            self.day = False
            self.empty_level()
            self.setup_level(self.settings.underground_map)
        else:
            self.day = True
            self.empty_level()
            self.setup_level(self.settings.end_map)

    def restart(self):
        self.day = True
        self.settings.powered = False
        self.settings.fire = False 
        if self.player.sprite.dead:
            self.game.lives -= 1
            self.game.sound.play_dead()
        self.empty_level()
        while self.game.sound.busy():
            pass
        self.game.sound.stop_bg()
        self.game.sound.play_bg()
        self.setup_level(self.level)

    def update(self):
        if self.goal.__len__() == 1:
            self.goal.update(self.world_shift)
            self.goal_collision()
        self.tiles.update(self.world_shift)
        self.warps.update(self.world_shift)
        self.blocks.update(self.world_shift)
        self.qblocks.update(self.world_shift)
        self.items.update(self.world_shift)
        self.enemies.update(self.world_shift)
        self.scroll_x()
        self.player.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.item_collision()
        self.enemy_collision()
        self.player.sprite.fballs.update(self.world_shift)

    
    def draw(self):
        if self.day == True:
            self.game.screen.fill(self.game.SKY)
        else:
            self.game.screen.fill(self.game.BLACK)
        if self.goal.__len__() == 1:
            self.goal.draw(self.display)
        self.tiles.draw(self.display)
        self.warps.draw(self.display)
        self.blocks.draw(self.display)
        self.qblocks.draw(self.display)
        self.items.draw(self.display)
        self.enemies.draw(self.display)
        self.player.draw(self.display)
        self.player.sprite.fballs.draw(self.display)

    def run(self):
        self.update()
        self.draw()

