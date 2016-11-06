import pygame
import random
from constants import *

class Bomb:
    def __init__(self, x):
        self.x = x
        self.y = -10
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, [self.x - 7, self.y - 7, 14, 14])

    def update(self):
        self.y += 5

    def handle_event(self, event):
        pass

    def is_out_of_screen(self):
        return self.y > 705
