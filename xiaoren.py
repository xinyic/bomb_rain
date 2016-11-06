import pygame
from constants import *

class Xiaoren:
    def __init__(self, x_xiaoren, y = 470):
        self.x = x_xiaoren
        self.y = y
        self.velocity = 0

    def draw(self, screen):
        head_x = self.x - 8
        head_y = self.y
        head_width = 16
        head_height = 15

        arm_start = [self.x - 10, self.y + head_height + 3]
        arm_end = [self.x + 10, self.y + head_height + 3]

        body_start = [self.x, self.y + head_height]
        body_end = [self.x, self.y + head_height + 8]

        leftleg_start =[self.x, self.y + head_height + 8]
        leftleg_end = [self.x - 10, 500]

        rightleg_start = [self.x, self.y + head_height + 8]
        rightleg_end = [self.x + 10, 500]

        pygame.draw.ellipse(screen, BLACK, [head_x, head_y, head_width, head_height], 2)
        pygame.draw.line(screen, BLACK, arm_start, arm_end, 2)
        pygame.draw.line(screen, BLACK, body_start, body_end, 2)
        pygame.draw.line(screen, BLACK, leftleg_start, leftleg_end, 2)
        pygame.draw.line(screen, BLACK, rightleg_start, rightleg_end, 2)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.velocity = 5
            if event.key == pygame.K_LEFT:
                self.velocity = -5
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT):
                self.velocity = 0

    def update(self):
        self.x += self.velocity
        self.x = self.x % 700



