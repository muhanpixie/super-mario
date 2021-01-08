import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SCREEN_W, SCREEN_H = 800, 600 # height of level map: 224
BG_SCALE = SCREEN_H/224
SCREEN_SIZE = (SCREEN_W, SCREEN_H)
PLAYER_SCALE = 2.9

CONS = {
    "player":{
        "speed":{
            "max_walk_speed":6,
            "max_run_speed": 12,
            "max_y_velocity": 11,
            "walk_acceleration": 0.15,
            "run_acceleration": 0.3,
            "jump_velocity": -10.5, 
            "turn_acceleration": 0.35,
        }
    },
    'gravity': 1.0,
}