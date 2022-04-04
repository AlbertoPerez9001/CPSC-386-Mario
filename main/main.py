import pygame as pg
import sys
from settings import Settings
from tiles import Tile
from level import Level
import game_functions as gf
from sound import Sound



class Game:
    BLACK = (0,0,0)
    SKY = (75, 132, 255)

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height
        self.lives = self.settings.player_lives
        self.sound = Sound()
        self.screen = pg.display.set_mode((self.screen_width,self.screen_height))
        pg.display.set_caption("Super Mario Bros")
        self.clock = pg.time.Clock()
        self.level = Level(self.settings.level_map,self.screen,game=self)
        
    def game_over(self):
        self.level.empty_level()
        self.screen.fill(self.BLACK)
        self.settings.player_coins = 0
        self.sound.play_game_over() 
        print('\nGAME OVER!\n\n')
        exit()

    def play(self):
        self.sound.play_bg()
        finished = False
        while not finished:
            self.level.run()
            gf.check_events(game=self)  
            if self.lives < 0:
                finished = True
            pg.display.update()
            self.clock.tick(60)
        self.game_over()

def main():
    g=Game()
    g.play()

if __name__=='__main__':
    main()