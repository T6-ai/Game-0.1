import pygame
from  pygame.locals import *
import sys

class Player:
    def __init__(self, x, y, width, height, x_direct, y_direct, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_direction = x_direct
        self.y_direction = y_direct
        self.vel = vel
    # def update_player_pos():
    #     global x
    #     global y
    #     global x_direction
    #     global y_direction
    #
    #     if self.x_direction > 0:
    #         if self.x < 600-self.width:
    #             self.x += self.x_direction + self.vel
    #     if self.x_direction < 0:
    #         if self.x > 0:
    #             self.x += self.x_direction + self.vel
    #
    #     if self.y_direction > 0:
    #         if self.y < 600-self.height:
    #             self.y += self.y_direction + self.vel
    #     if self.y_direction < 0:
    #         if self.y > 0:
    #             self.y += self.y_direction + self.vel



    def draw(self, screen):
        pygame.draw.rect(screen, (200,200,255), (self.x, self.y, self.width, self.height))
