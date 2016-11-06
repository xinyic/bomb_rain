import pygame
from constants import *

class Xiaoren:
    def __init__(self, x):
        self.x = x
        self.y = WINDOW_HEIGHT - 15
        self.velocity = 0

    def draw(self, screen):
        head_x = self.x - 8
        head_y = self.y - 15
        head_width = 16
        head_height = 15

        arm_start = [self.x - 10, self.y + head_height - 12]
        arm_end = [self.x + 10, self.y + head_height - 12]

        body_start = [self.x - 1, self.y + head_height - 17]
        body_end = [self.x - 1, self.y + head_height - 7]

        leftleg_start =[self.x, self.y + head_height - 7]
        leftleg_end = [self.x - 10, self.y + 15]

        rightleg_start = [self.x, self.y + head_height - 7]
        rightleg_end = [self.x + 10, self.y + 15]

        pygame.draw.ellipse(screen, BLACK, [head_x, head_y, head_width, head_height], 2)
        pygame.draw.line(screen, BLACK, arm_start, arm_end, 2)
        pygame.draw.line(screen, BLACK, body_start, body_end, 2)
        pygame.draw.line(screen, BLACK, leftleg_start, leftleg_end, 2)
        pygame.draw.line(screen, BLACK, rightleg_start, rightleg_end, 2)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.velocity = XIAOREN_SPEED
            if event.key == pygame.K_LEFT:
                self.velocity = -XIAOREN_SPEED
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_RIGHT and self.velocity == XIAOREN_SPEED) or \
               (event.key == pygame.K_LEFT and self.velocity == -XIAOREN_SPEED):
                self.velocity = 0

    def update(self):
        self.x += self.velocity
        self.x = self.x % WINDOW_WIDTH



