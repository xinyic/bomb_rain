import pygame
from constants import *
from game import Game

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Bomb Rain")
clock = pygame.time.Clock()

game = Game()

while not game.game_over:
    for e in pygame.event.get():
        game.handle_event(e)

    game.update()

    screen.fill(WHITE)
    game.draw(screen)
    pygame.display.flip()
 
    clock.tick(60)

pygame.quit()