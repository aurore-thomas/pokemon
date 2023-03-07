import pygame as pg

class Button:
    def __init__(self, image, text, font, pos, size, basic_color, hovering_color, action):
        self.image = image
        self.action = action
        self.font = font 
        self.text = font.render(text, True, basic_color)
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.x_size = size[0]
        self.y_size = size[1]
        self.basic_color = basic_color
        self.hovering_color = hovering_color
        if image is None:
            self.image = self.text
        else:
            self.image = pg.transform.scale(image, int(size[0]), int(size[1]))
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def draw(self, win):
        if self.image is not None:
            win.blit(self.image, self.rect)
        win.blit(self.text, self.rect)

    def button_clicked(self, win):
        self.mouse = pg.mouse.get_pos() # It gives us information about the mouse's position
        self.click = pg.mouse.get_pressed() # It gives information about the number of click
        if self.image == self.text :
            if (self.x_pos + self.x_size) > self.mouse[0] > self.x_pos and (self.y_pos + self.y_size) > self.mouse[1] > self.y_pos:
                self.basic_color = self.hovering_color
                win.blit(self.text, self.rect)
                pg.display.update()
        if self.click[0] == 1 and self.action != None:
            self.action()
                
        
        
