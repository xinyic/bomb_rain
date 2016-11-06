import pygame
import random
from objects.xiaoren import Xiaoren
from objects.bomb import Bomb
from constants import *

class Playing:
    def __init__(self):
        self.xiaoren = Xiaoren(WINDOW_WIDTH / 2)
        self.bombs = []
        self.game_over = False

    def all_game_objects(self):
        return self.bombs + [self.xiaoren]

    def draw(self, screen):
        for o in self.all_game_objects():
            o.draw(screen)

    def update(self):
        should_create_bomb = (random.randint(0, 10) == 3)
        if should_create_bomb:
            self.bombs.append(Bomb(random.randint(0, WINDOW_WIDTH)))

        for o in self.all_game_objects():
            o.update()

        for b in self.bombs:
            if b.is_out_of_screen():
                self.bombs.remove(b)

        if self.check_explosion() is not None:
            self.game_over = True
            
    def handle_event(self, event):
        for o in self.all_game_objects():
            o.handle_event(event)

    def check_explosion(self):
        for b in self.bombs:
            if (b.y > WINDOW_HEIGHT - 23) and abs(b.x - self.xiaoren.x) < 15:
                return b
        return None

    def next_stage(self):
        if self.game_over:
            return Playing()
        else:
            return None
