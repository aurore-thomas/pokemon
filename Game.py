# import pygame as pg
import sys
import json
from Class.Fight import Fight
from Class.Pokemon import Pokemon
from Class.Settings import *
from Class.Buttons import Button

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Attrapez-les tous !")
        self.win = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.running = True

    def run(self):
        # Background :
        self.menu_background = pg.image.load("Pictures/Other/background_menu.png")
        self.win.blit(self.menu_background, (0,0))

        # Title :
        self.title_menu = pg.image.load("Pictures/Other/pokemon_title.png")
        self.title_menu = pg.transform.scale(self.title_menu, (500, 203))
        self.title_rect = self.title_menu.get_rect(center=(WIN_RES[0]/2, 200))
        self.win.blit(self.title_menu, self.title_rect)

        # Buttons :
        self.button_play = Button(None, "PLAY", NORMAL_FONT, (500,500), (200,200), WHITE, BLACK, quit)

        while self.running:
            self.button_play.draw(self.win)
            self.button_play.button_clicked(self.win)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            pg.display.update()

if __name__ == '__main__':
    menu = Game()
    menu.run()
    