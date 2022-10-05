import pygame
from pygame.locals import *

class Square:
  def __init__(self, x, y, height, width, shade, name):
    self.x = x
    self.y = y
    self.height = height
    self.width = width
    self.shade = shade
    self.name = name
    self.controller = pygame.Surface((height, width))
    self.color = (140, 140, 140) if self.shade == 'dark' else (200, 200, 200)
    self.occupied = False
    self.owner = None

  def __str__(self):
    return f"""
      name: {self.name}
      shade: {self.shade}
      color: {self.color}
      occupied: {self.occupied}
      owner: {self.owner.name}
    """

  def occupy(self, piece):
    self.occupied = True
    self.owner = piece
  
  def clear(self):
    self.occupied = False
    self.owner = None