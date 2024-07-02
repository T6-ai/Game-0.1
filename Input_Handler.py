import pygame
from  pygame.locals import *


class Input:
    def __init__(self, player_instance):
        self.player = player_instance

    def handle_event(self, event):
        if event.type == KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                print("a")
                self.player.x -= self.vel
