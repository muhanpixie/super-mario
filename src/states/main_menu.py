import pygame
from ..game import random_color, get_img
from .. import cfg, setup
from ..cmp import info

class MainMenu:
    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor()
        self.info = info.Info('main_menu')
        self.done = False
        self.next = 'load_screen'
    
    def setup_background(self):
        self.background = setup.graphics.get('level_1')
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background,
            (
                int(self.background_rect.width * cfg.BG_SCALE), 
                int(self.background_rect.height * cfg.BG_SCALE),
            )
        )
        self.background_rect = self.background.get_rect()
        self.viewport = setup.screen.get_rect()
        self.caption = get_img(setup.graphics['title_screen'], 1, 60, 176, 88, scale=cfg.BG_SCALE)
    def setup_player(self):
        pass

    def setup_cursor(self):
        self.cursor = pygame.sprite.Sprite()
        self.cursor.image = get_img(setup.graphics['item_objects'], 25, 160, 6, 8, scale= cfg.BG_SCALE)
        self.cursor.rect = self.cursor.image.get_rect()
        self.cursor.rect.topleft = (220,360)
        self.cursor.state = '1p'

    def update(self, surface, keys):
        self.update_cursor(keys)
        surface.blit(self.background, (0,0))
        surface.blit(self.caption, (170, 100))
        surface.blit(self.cursor.image, self.cursor.rect)
        self.info.update()
        self.info.draw(surface)

    def update_cursor(self, keys):
        if keys[pygame.K_UP]:
            self.cursor.state = '1p'
            self.cursor.rect.y = 360
        elif keys[pygame.K_DOWN]:
            self.cursor.state = '2p'
            self.cursor.rect.y = 405
        elif keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
            if self.cursor.state == '1p':
                self.done = True
            else:
                self.done = True