import pygame

from .. import setup, cfg
from ..game import get_img

class Player(pygame.sprite.Sprite):
    def __init__(self, name='test-name'):
        super().__init__()
        self.name = name
        self.setup_states()
        self.setup_velocities()
        self.setup_timers()
        self.load_images()
        

    def setup_states(self):
        self.face_right = True
        self.dead = False
        self.big = False
        self.state = 'stand'

    def setup_velocities(self):
        self.x_vel, self.y_vel = 0, 0
        for k, v in cfg.CONS['player']['speed'].items():
            setattr(self, k, v)
        self.gravity = cfg.CONS.get('gravity',1)
        self.max_x_vel = self.max_walk_speed
        self.x_acceleration = self.walk_acceleration
    #---end of setup velocities
    def setup_timers(self):
        self.walking_timer = 0
        self.transition_timer = 0

    def load_images(self):
        sheet = setup.graphics['mario_bros']
        frames = []
        r_frames = []
        l_frames = []
        frame_rects = [
            (178,32,12,16),
            (80,32,15,16),
            (96,32,16,16),
            (112,32,16,16),
        ]

        for r in frame_rects:
            r_image = get_img(sheet, *r, None, cfg.PLAYER_SCALE)
            l_image = pygame.transform.flip(r_image, 1, 0)
            r_frames.append(r_image)
            l_frames.append(l_image)
        
        self.r_frames = r_frames
        self.l_frames = l_frames
        
        frames.append(get_img(sheet, 178,32,12,16,None,cfg.PLAYER_SCALE))
        self.frames = r_frames
        self.frame_idx = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect()

    def update(self, keys):
        curtime = pygame.time.get_ticks()
        self.handle_states(keys)
        self.image = self.frames[self.frame_idx]
    #---end of update

    def handle_states(self, keys):
        if self.state == 'stand':
            self.stand(keys)
        elif self.state == 'walk':
            self.walk(keys)
        elif self.state == 'jump':
            self.jump(keys)

    def stand(self, keys):
        self.frame_idx = 0
        self.x_vel, self.y_vel = 0, 0
        if keys[pygame.K_RIGHT]:
            self.face_right = True
            self.state = 'walk'
        elif keys[pygame.K_LEFT]:
            self.face_right = False
            self.state = 'walk'

    def walk(self,keys):
        if keys[pygame.K_s]:
            self.max_x_vel = self.max_run_speed
            self.x_acceleration = self.run_acceleration
        else:
            self.max_x_vel = self.max_walk_speed
            self.x_acceleration = self.walk_acceleration
        curtime = pygame.time.get_ticks()
        if curtime - self.walking_timer > 100:
            self.frame_idx += 1
            self.frame_idx %= 3
            self.walking_timer = curtime
        if keys[pygame.K_RIGHT]:
            self.face_right = True
            if self.x_vel < 0: #moving left
                self.frame_idx = 0
                self.frames = self.l_frames
                self.x_acceleration = self.turn_acceleration
            self.x_vel = self.cal_vel(self.x_vel, self.x_acceleration, self.max_x_vel, 1)
        elif keys[pygame.K_LEFT]:
            self.face_right = False
            if self.x_vel > 0:# moving right
                self.frame_idx = 0
                self.frames = self.r_frames
                self.x_acceleration = self.turn_acceleration
            self.x_vel = self.cal_vel(self.x_vel, self.x_acceleration, self.max_x_vel, 0)
        else: # not left or right
            if self.face_right:
                self.x_vel -= self.x_acceleration
                if self.x_vel < 0:
                    self.x_vel = 0
                    self.state = 'stand'
            else:
                self.x_vel += self.x_acceleration
                # self.x_vel += self.x_acceleration
                if self.x_vel > 0:
                    self.x_vel = 0
                    self.state = 'stand'

    def cal_vel(self, vel, acc, max_vel, positive=True):
        if positive:
            return min(vel+acc, max_vel)
        else:
            return max(vel-acc, -max_vel)