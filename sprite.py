import math
import pygame


class Sprite:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.sizeX = 100
        self.sizeY = 100

        self.direction = 0

        self.color = 'black'
        self.hidden = False

    def draw(self, screen):
        if not self.hidden:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.sizeX, self.sizeY))

    def hide(self):
        self.hidden = True

    def show(self):
        self.hidden = False

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move(self, steps):
        self.x += steps * math.sin(math.radians(self.direction))
        self.y += steps * math.cos(math.radians(self.direction))

    def turn(self, degrees):
        self.direction += degrees

    def set_direction(self, direction):
        self.direction = direction
