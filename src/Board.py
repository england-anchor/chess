from turtle import color
import pygame
import os
from pygame.locals import *
from Square import Square
from coordinates import *
from Piece import Piece
from Rook import Rook
from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from King import King
from Queen import Queen

class Board:
  def __init__(self, height, width, color):
    self.height = height
    self.width = width
    self.color = color
    self.pieces = []
    self.squares = []
    self.controller = pygame.Surface((height, width))

  def load_squares(self):
    square_width = self.width / 8
    square_height = self.height / 8
    self.piece_height = square_height * 0.85
    self.piece_width = square_width * 0.85
    current_y = self.height - square_height
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    color_schema = ['dark', 'light', 'dark', 'light', 'dark', 'light', 'dark', 'light']
    for file in range(8):
      current_x = 0
      for rank in range(8):
        self.squares.append(Square(
          current_x, 
          current_y, 
          square_height, 
          square_width, 
          color_schema[rank],
          ( str(letters[rank]) + str((file+1)) )
        ))
        current_x = current_x + square_width
        if rank == 7:
          color_schema.reverse()
          current_y = current_y - square_height

  def print_squares(self):
    for square in self.squares:
      print(f'''
        x: {square.x}
        y: {square.y}
        shade: {square.shade}
        name: {square.name}
        occupied: {square.occupied}
      ''')

  def print_active_squares(self):
    active = []
    for square in self.squares:
      if square.owner != None:
        active.append(square)
        print(square)
    print(len(active))

  def load_pieces(self):
    
    self.build_rooks()
    self.build_pawns()
    self.build_knights()
    self.build_bishops()
    self.build_queens()
    self.build_kings()

    for square in self.squares:
      for piece in self.pieces:
        if square.name == piece.current_square:
          square.occupy(piece)

  def draw_squares(self):
    for square in self.squares:
      self.controller.blit(square.controller, (square.x, square.y))
      square.controller.fill(square.color)
      if square.owner != None:
          square.controller.blit(square.owner.controller, pos_center(square.owner, square))

  def list_active_pieces(self):
    for square in self.squares:
      if square.occupied == True:
        print(square)

  def build_rooks(self):
    white_home_squares = ['A1', 'H1']
    black_home_squares = ['A8', 'H8']
    white_rook_image = pygame.image.load(os.path.join('Assets', 'white_rook.png'))
    black_rook_image = pygame.image.load(os.path.join('Assets', 'black_rook.png'))
    for i in range(2):
      self.pieces.append(Rook(
        ( 'white_rook_' + str(i) ),
        white_home_squares[i],
        white_rook_image,
        self.piece_height,
        self.piece_width,
        'white'
      ))
    for i in range(2):
      self.pieces.append(Rook(
        ( 'black_rook_' + str(i) ),
        black_home_squares[i],
        black_rook_image,
        self.piece_height,
        self.piece_width,
        'black'
      ))

  def build_pawns(self):
    white_home_squares = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2']
    black_home_squares = ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7']
    white_pawn_image = pygame.image.load(os.path.join('Assets', 'white_pawn.png'))
    black_pawn_image = pygame.image.load(os.path.join('Assets', 'black_pawn.png'))
    for i in range(8):
      self.pieces.append(Pawn(
        ('white_pawn_' + str(i)),
        white_home_squares[i],
        white_pawn_image,
        self.piece_height,
        self.piece_width,
        'white'
      ))
    for i in range(8):
      self.pieces.append(Pawn(
        ('black_pawn_' + str(i)),
        black_home_squares[i],
        black_pawn_image,
        self.piece_height,
        self.piece_width,
        'black'
      ))
  
  def build_knights(self):
    white_home_squares = ['B1', 'G1']
    black_home_squares = ['B8', 'G8']
    white_knight_image = pygame.image.load(os.path.join('Assets', 'white_knight.png'))
    black_knight_image = pygame.image.load(os.path.join('Assets', 'black_knight.png'))
    for i in range(2):
      self.pieces.append(Knight(
        ('white_knight_' + str(i)),
        white_home_squares[i],
        white_knight_image,
        self.piece_height,
        self.piece_width,
        'white'
      ))
    for i in range(2):
      self.pieces.append(Knight(
        ('black_knight_' + str(i)),
        black_home_squares[i],
        black_knight_image,
        self.piece_height,
        self.piece_width,
        'black'
      ))

  def build_bishops(self):
    white_home_squares = ['C1', 'F1']
    black_home_squares = ['C8', 'F8']
    white_bishop_image = pygame.image.load(os.path.join('Assets', 'white_bishop.png'))
    black_bishop_image = pygame.image.load(os.path.join('Assets', 'black_bishop.png'))
    for i in range(2):
      self.pieces.append(Bishop(
        ('white_knight_' + str(i)),
        white_home_squares[i],
        white_bishop_image,
        self.piece_height,
        self.piece_width,
        'white'
      ))
    for i in range(2):
      self.pieces.append(Bishop(
        ('black_knight_' + str(i)),
        black_home_squares[i],
        black_bishop_image,
        self.piece_height,
        self.piece_width,
        'black'
      ))

  def build_queens(self):
    white_queen_image = pygame.image.load(os.path.join('Assets', 'white_queen.png'))
    black_queen_image = pygame.image.load(os.path.join('Assets', 'black_queen.png'))
    self.pieces.append(Queen(
        'white_queen',
        'E1',
        white_queen_image,
        self.piece_height,
        self.piece_width,
        'white'
    ))
    self.pieces.append(Queen(
        'black_queen',
        'D8',
        black_queen_image,
        self.piece_height,
        self.piece_width,
        'black'
    ))

  def build_kings(self):
    white_king_image = pygame.image.load(os.path.join('Assets', 'white_king.png'))
    black_king_image = pygame.image.load(os.path.join('Assets', 'black_king.png'))
    self.pieces.append(King(
        'white_king',
        'D1',
        white_king_image,
        self.piece_height,
        self.piece_width,
        'white'
    ))
    self.pieces.append(King(
        'black_king',
        'E8',
        black_king_image,
        self.piece_height,
        self.piece_width,
        'black'
    ))

