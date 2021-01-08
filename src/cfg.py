import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SCREEN_W, SCREEN_H = 800, 600 # height of level map: 224
BG_SCALE = SCREEN_H/224
SCREEN_SIZE = (SCREEN_W, SCREEN_H)