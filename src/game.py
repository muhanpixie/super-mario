import os, random
import pygame as pg

from . import cfg, setup

class Game:
    def __init__(self):
        self.screen = setup.screen
        self.clock = setup.clock
        self.keys = pg.key.get_pressed()

    def run(self, state):
        while 1:
            for e in pg.event.get():
                keys = pg.key.get_pressed()
                if e.type == pg.QUIT:
                    return
                elif e.type == pg.KEYDOWN:
                    self.keys = keys
                    if keys[pg.K_ESCAPE]:
                        return
                elif e.type == pg.KEYUP:
                    self.keys = keys
            self.screen.fill((0,23,122))
            state.update(self.screen, keys)

            pg.display.update()
            self.clock.tick(10)


def load_all_images(path, accept=(".jpg",".png")):
    ans = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if not ext.lower() in accept:
            continue
        img = pg.image.load(os.path.join(path, pic))
        if img.get_alpha():
            img = img.convert_alpha()
        else:
            img = img.convert()
        ans[name] = img
    return ans

def get_img(src, x, y, w, h, key=None, scale=1):
    '''抠图'''
    ans = pg.Surface((w, h))
    ans.blit(src, (0,0), (x, y, w, h))
    if not key:
        key = ans.get_at((0,0))
    ans.set_colorkey(key)
    ans = pg.transform.scale(ans, (int(w*scale), int(h*scale)))
    return ans

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)