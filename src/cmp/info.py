import pygame
from .coin import FlashingCoin

pygame.font.init()

class Info:
    def __init__(self, state):
        self.state = state
        self.create_state_labels()
        self.create_info_lables()
        self.flash_coin = FlashingCoin()
    
    def create_state_labels(self):
        labels = []
        if self.state == 'main_menu':
            labels.append((self.create_label('1 player game'), (272,360)))
            labels.append((self.create_label('2 player game'), (272,405)))
            labels.append((self.create_label('TOP -'),(290,465)))
            labels.append((self.create_label('00000'), (400, 465)))
        self.state_labels = labels
    def create_info_lables(self):
        pass

    def create_label(self, label, size=40, w_scale=1.25, h_scale=1):
        font = pygame.font.SysFont(None, size)
        label_img = font.render(label, 1, (255, 255, 255))
        return label_img

    def draw(self, surface):
        for label in self.state_labels:
            surface.blit(label[0], label[1])
        surface.blit(self.flash_coin.image, self.flash_coin.rect)

    def update(self):
        self.flash_coin.update()