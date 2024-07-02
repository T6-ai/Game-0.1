import pygame
from  pygame.locals import *
import sys
import player
import Input_Handler

pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT =600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
player_instance = player.Player(200, 200, 50, 50, 0, 0, 3)
input_handler = Input_Handler.Input(player_instance)


def main():
    global screen
    while True:
        dt = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
                #SCREEN
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        screen.fill((66, 71, 120))


        input_handler.handle_event(event)
        player_instance.draw(screen)


        pygame.display.update()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
pygame.quit()
