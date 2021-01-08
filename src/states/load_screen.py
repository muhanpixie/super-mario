import pygame

from ..cmp import info

class LoadScreen:
    def __init__(self):
        self.done = False
        self.next = 'level'
        self.timer = 0
        self.loading_time = 1_500 #1.5 second
        self.info = info.Info('load-screen')

    def update(self, surface, keys):
        self.draw(surface)
        current_time = pygame.time.get_ticks()
        if self.timer == 0:
            self.timer = current_time
        elif current_time - self.timer > self.loading_time:
            self.done = True
            self.timer = 0

    def draw(self, surface):
        surface.fill((0,0,0))
        self.info.draw(surface)