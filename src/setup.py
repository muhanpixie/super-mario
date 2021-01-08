import os
import pygame 
from . import cfg
from .game import load_all_images


pygame.init()
screen = pygame.display.set_mode(cfg.SCREEN_SIZE)
clock = pygame.time.Clock()
graphics = load_all_images(os.path.join(cfg.BASE_DIR, 'resources', 'graphics'))