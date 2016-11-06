import pygame

class Losing:
    def __init__(self, xiaoren, bombs, exploded_bomb):
        self.xiaoren = xiaoren
        self.bombs = bombs[:]
        self.bombs.remove(exploded_bomb)
        self.exploded_bomb = exploded_bomb
        self.flash_tick = 60

    def update(self):
        self.flash_tick -= 1

    def handle_event(self, event):
        pass

    def draw(self, screen):
        if (self.flash_tick / 15) % 2 == 0:
            self.xiaoren.draw(screen)
            self.exploded_bomb.draw(screen)
        for b in self.bombs:
            b.draw(screen)

    def next_stage(self):
        if self.flash_tick == 0:
            # Delay import Playing here to break the import cycle between the stages. 
            from playing import Playing

            return Playing()
        return None
