import pygame
from stages.playing import Playing

class Game:
    def __init__(self):
        self.done = False
        self.current_stage = Playing()

    def update(self):
        self.current_stage.update()

        next_stage = self.current_stage.next_stage()
        if next_stage is not None:
            self.current_stage = next_stage        

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.done = True

        self.current_stage.handle_event(event)

    def draw(self, screen):
        self.current_stage.draw(screen)
