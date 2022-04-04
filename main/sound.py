import pygame as pg

class Sound:
    def __init__(self):
        pg.mixer.init()
        self.jumpsound = pg.mixer.Sound('audio/Mario Jump - Gaming Sound Effect (HD).mp3')
        self.jumpsound.set_volume(0.1)
        self.breaksound = pg.mixer.Sound('audio/[Super Mario Bros] Block Sound Effect [Free Ringtone Download].mp3')
        self.coinsound = pg.mixer.Sound('audio/Super Mario coin sound (!).mp3')
        self.powerupsound = pg.mixer.Sound('audio/Super Mario Power Up Sound Effect.mp3') 
        self.powerdownsound = pg.mixer.Sound('audio/Super Mario Power Down Sound Effect.mp3') 
        self.warp = pg.mixer.Sound('audio/Super Mario Bros Pipe Sound Effect.mp3') 
        self.dead = pg.mixer.Sound('audio/Mario Death - Sound Effect.mp3')
        self.cleared = pg.mixer.Sound('audio/Super Mario Bros. Music - Level Clear.mp3')
        self.game_over = pg.mixer.Sound('audio/Super Mario Bros. - Game Over Sound Effect.mp3')

    def play_music(self, music, volume=0.3):
        pg.mixer.music.unload()           
        pg.mixer.music.load(music)
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.play(-1, 0.0)

    def busy(self): return pg.mixer.get_busy()
    def play_sound(self, sound, lp=0): pg.mixer.Sound.play(sound, loops = lp)
    
    def play_bg(self): self.play_music('audio/Super Mario Bros (NES) Music - Overworld Theme.mp3',volume = 1)
    def stop_bg(self): pg.mixer.music.stop()

    def play_game_over(self):
        self.stop_bg()     
        self.play_sound(self.game_over)
        while self.busy():  
            pass

    def play_jump(self): self.play_sound(self.jumpsound)
    def play_break(self): self.play_sound(self.breaksound)
    def play_coin(self): self.play_sound(self.coinsound)
    def play_pow_up(self): self.play_sound(self.powerupsound)
    def play_pow_down(self): self.play_sound(self.powerdownsound)
    def play_warp(self): self.play_sound(self.warp)
    def play_end_level(self): 
        self.stop_bg()     
        self.play_sound(self.cleared)
        while self.busy():  
            pass
    def play_dead(self): 
        pg.mixer.stop()
        self.play_sound(self.dead)