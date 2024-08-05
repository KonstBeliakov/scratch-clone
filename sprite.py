import math
import random

import pygame
from pygame import *
from utils import *


class Sprite:
    def __init__(self, screen):
        self.x = 0
        self.y = 0

        self.sizeX = 100
        self.sizeY = 100

        self.direction = 0

        self.color = 'black'
        self.hidden = False

        self.screen = screen

    def draw(self, screen):
        if not self.hidden:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.sizeX, self.sizeY))

    def hide(self):
        self.hidden = True

    def show(self):
        self.hidden = False

    def go_to(self, x, y):
        self.x = x
        self.y = y

    def go_to_random_position(self):
        size = self.screen.get_size()
        self.x = random.randrange(size[0])
        self.y = random.randrange(size[1])

    def move(self, steps):
        self.x += steps * math.sin(math.radians(self.direction))
        self.y += steps * math.cos(math.radians(self.direction))

    def turn(self, degrees):
        self.direction += degrees

    def set_direction(self, direction):
        self.direction = direction

    def if_on_edge_bounce(self):
        pass

    def set_color(self, color):
        self.color = color

    def touching(self, sprite2):
        pass
