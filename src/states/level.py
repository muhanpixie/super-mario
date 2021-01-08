import pygame

from ..cmp import info, player
from .. import setup, cfg

class Level:
    def __init__(self, level=1):
        self.done = False
        self.next = None
        self.level = level
        self.info = info.Info('level')
        self.setup_background()
        self.setup_play()

    def setup_background(self):
        self.bg = setup.graphics['level_1']
        rect = self.bg.get_rect()
        self.bg = pygame.transform.scale(self.bg,
            (
                int(rect.width * cfg.BG_SCALE), 
                int(rect.height * cfg.BG_SCALE)
            ))
        self.rect = self.bg.get_rect()
        self.game_window = setup.screen.get_rect()

    def setup_play(self):
        self.player = player.Player()
        self.player.rect.topleft = 300,490

    def update(self, surface, keys):
        self.player.update(keys)
        self.update_player_position()
        self.update_game_window()
        self.draw(surface)

    def update_game_window(self):
        self.game_window.x += self.player.x_vel

    def update_player_position(self):
        # self.player.rect.x += self.player.x_vel
        self.player.rect.y += self.player.y_vel

    def draw(self, surface):
        surface.blit(self.bg, (0,0), self.game_window)
        surface.blit(self.player.image, self.player.rect)
        self.info.draw(surface)