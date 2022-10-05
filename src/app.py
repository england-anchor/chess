import pygame
import os
from coordinates import *
from Board import *
from Window import Window
from Rook import Rook

#settings
FPS = 60
pygame.display.set_caption("Chess")
white = (255, 255, 255)
gray = (140, 140, 140)


window = Window(500, 500, white)
board = Board((window.height  * .80), (window.width * .80), gray)
board.load_squares()
board.load_pieces()
board.print_active_squares()

def draw_window():
    window.controller.fill(window.color)
    window.draw_board(board)
    board.draw_squares()
    pygame.display.update()

def main():
  clock = pygame.time.Clock()
  run = True
  while run:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      
      draw_window()

  pygame.quit()

if __name__ == '__main__':
  main()