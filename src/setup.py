import os
import pygame 
from . import cfg
from .game import load_all_images
from src.states import main_menu, load_screen, level

pygame.init()
screen = pygame.display.set_mode(cfg.SCREEN_SIZE)
clock = pygame.time.Clock()
graphics = load_all_images(os.path.join(cfg.BASE_DIR, 'resources', 'graphics'))

states = {
    'main_menu': main_menu.MainMenu(),
    'load_screen': load_screen.LoadScreen(),
    'level': level.Level(),
}