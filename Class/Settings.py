import pygame as pg
import json
import sys
import requests

# We have to initialize Pygame to import the fonts
pg.init() 
running = True

FPS = 60
WIN_RES = (1000, 700)

BEGIN_SCREEN = pg.font.Font('Fonts/OmegaRuby.ttf', 70)
NORMAL_FONT = pg.font.Font('Fonts/Pokemon Classic.ttf', 20)
FONT_PATH = 'Fonts/Pokemon Classic.ttf'

WHITE = (255, 255, 255)
BLACK = (25, 25, 25)

# To have a complete list of Pokemon, we use an API :
url_api = 'https://pokeapi.co/api/v2'