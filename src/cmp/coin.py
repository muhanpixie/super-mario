import pygame

from .. import setup, cfg
from ..game import get_img

class FlashingCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frames = []
        self.frame_index = 0
        rects = [
            (1,160,5,8), (9,160,5,8), (17,160,5,8), (9,160,5,8),
        ]
        self.load_frames(rects)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 58  
        self.timer = 0

    def load_frames(self, rects):
        sheet = setup.graphics['item_objects']
        for frame_rect in rects:
            self.frames.append(get_img(sheet, *frame_rect, (0,0,0), cfg.BG_SCALE))

    def update(self):
        self.current_time = pygame.time.get_ticks()
        durs = [375,125,125,125]
        if self.timer == 0:
            self.timer = self.current_time
        elif self.current_time - self.timer > durs[self.frame_index]:
            self.frame_index += 1
            self.frame_index %= 4
            self.timer = self.current_time
        self.image = self.frames[self.frame_index]