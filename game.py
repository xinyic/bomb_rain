import pygame
import random
from xiaoren import Xiaoren
from bomb import Bomb
from constants import *

class Game:
    def __init__(self):
        self.xiaoren = Xiaoren(350)
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
            self.bombs.append(Bomb(random.randint(0, 700)))

        for o in self.all_game_objects():
            o.update()

        for b in self.bombs:
            if b.is_out_of_screen():
                self.bombs.remove(b)

        if self.check_explosion() is not None:
            self.game_over = True
            
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.game_over = True

        for o in self.all_game_objects():
            o.handle_event(event)

    def check_explosion(self):
        for b in self.bombs:
            if b.y > 477 and abs(b.x - self.xiaoren.x) < 15:
                return b
        return None
