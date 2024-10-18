import pygame
from Board import Board
from Game import Game

pygame.init()

class Checkers:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.FPS = pygame.time.Clock()

    def _draw(self, board):
        board.draw(self.screen)
        pygame.display.update()

    def main(self, window_width, window_height):
        board_size = 8
        tidle_width, title_height = window_width // board_size, window_height // board_size
        board = Board(tidle_width, title_height, board_size)
        game = Game()
        while self.running:
            game.check_jump(board)

            for self.event in pygame.event.get():
                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    board.handle_click(self.event.pos)

                else:
                    game.message()
                    self.running = False

            self._draw(board)
            self.FPS.tick(60)

