import pygame as pg
import sys
from pygame.locals import *

pg.init()
font = pg.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def calorieMenuScreen(self):
    loggingCalories = True
    while loggingCalories:

        self.screen.fill((0, 0, 0))
        draw_text("calorieMenu", font, (255, 255, 255), self.screen, 20, 20)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_e:
                    loggingCalories = False

        pg.display.update()