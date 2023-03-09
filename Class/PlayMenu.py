from Class.Settings import *
from Class.Buttons import Button

class PlayMenu:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Attrapez-les tous !")
        self.win = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.running = True

        with open("Json/save_player.json", "r", encoding='utf-8') as file:
            self.information = json.load(file)
        

    def draw(self):
        # Background :
        self.menu_background = pg.image.load("Pictures/Other/background_choice.png")
        self.win.blit(self.menu_background, (0,0))

        # Character :
        # if self.information["character"] == "girl":
        #     self.character = pg.image.load("Pictures/Other/girl.png")
        # else:
        #     self.character = pg.image.load("Pictures/Other/boy.png")
        # self.win.blit(self.character, (100, 100))

        # Textbox:
        self.textbox = pg.image.load("Pictures/Other/textbox.png")
        self.textbox = pg.transform.scale(self.textbox, (int(self.textbox.get_width())*3.5, int(self.textbox.get_height())*3.5))
        self.textbox_position = self.textbox.get_rect(center=(WIN_RES[0]/2, 610))
        self.win.blit(self.textbox, self.textbox_position)

    def event(self):
        self.mouse_pos = pg.mouse.get_pos()

        for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()

    def update(self):
        pass

    def run(self):
        while self.running:
            self.draw()
            self.event()
            self.update()
            pg.display.update()