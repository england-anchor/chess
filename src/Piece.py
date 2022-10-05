import pygame
from pygame.locals import *

class Piece:
  def __init__(self, name, current_square, image, height, width, color):
    self.name = name
    self.current_square = current_square
    self.image = image
    self.height = height
    self.width = width
    self.color = color
    self.active = True
    self.moves = []
    self.controller = pygame.transform.scale(self.image, (self.width, self.height))

  def __str__(self):
    return f'''
      name: {self.name}
      current_square: {self.current_square}
      color: {self.color}
      height: {self.height}
      width: {self.width}
      moves: {self.moves}
      controller: {self.controller}
    '''