import pygame
from pygame.locals import *
from coordinates import *

class Window:
  def __init__(self, height, width, color):
    self.height = height
    self.width = width
    self.color = color
    self.controller = pygame.display.set_mode((height, width))

  def draw_board(self, board):
    self.controller.blit(board.controller, pos_center(board, self))
    board.controller.fill(board.color)
