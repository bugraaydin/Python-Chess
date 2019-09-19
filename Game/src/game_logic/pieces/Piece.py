import pygame
import json

from config import PossibleMoveJSONGenerator
from config.Config import Config as cfg


class Piece:
    def __init__(self, x_file, y_file, color, TYPE):
        self.x_file = x_file
        self.y_file = y_file
        self.color = color
        self.TYPE = TYPE
        self.image_path = ""
        self.possible_moves = []
        self.is_selected = False

        if (self.color == "black"):
            if (self.TYPE == "K"):
                self.image_path = "media/pieces/black/king.png"
            elif (self.TYPE == "Q"):
                self.image_path = "media/pieces/black/queen.png"
            elif (self.TYPE == "R"):
                self.image_path = "media/pieces/black/rook.png"
            elif (self.TYPE == "B"):
                self.image_path = "media/pieces/black/bishop.png"
            elif (self.TYPE == "N"):
                self.image_path = "media/pieces/black/knight.png"
            elif (self.TYPE == "P"):
                self.image_path = "media/pieces/black/pawn.png"
        else:
            if (self.TYPE == "K"):
                self.image_path = "media/pieces/white/king.png"
            elif (self.TYPE == "Q"):
                self.image_path = "media/pieces/white/queen.png"
            elif (self.TYPE == "R"):
                self.image_path = "media/pieces/white/rook.png"
            elif (self.TYPE == "B"):
                self.image_path = "media/pieces/white/bishop.png"
            elif (self.TYPE == "N"):
                self.image_path = "media/pieces/white/knight.png"
            else:
                self.image_path = "media/pieces/white/pawn.png"

        self.image = pygame.image.load(self.image_path)
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(cfg.display_width / 8), int(cfg.display_height / 8)))

        possible_moves = PossibleMoveJSONGenerator.generate_possible_moves()
        if self.TYPE == "P":
            selected_index = 0
            if self.color == "black":
                selected_index = 1
            for move in possible_moves[self.TYPE][selected_index]:
                self.possible_moves.append(move)
        else:
            for move in possible_moves[self.TYPE]:
                self.possible_moves.append(move)

    def update_pawn_first_move(self):
        if self.color == "black" and self.y_file == 1:
            self.possible_moves.remove([0, -2])
        if self.color == "white" and self.y_file == 6:
            self.possible_moves.remove([0, 2])

    def castle_not_possible(self):
        if self.color == "black":
            try:
                self.possible_moves.remove([-2, 0])
                self.possible_moves.remove([3, 0])
            except:
                pass
        else:
            try:
                self.possible_moves.remove([2, 0])
                self.possible_moves.remove([-3, 0])
            except:
                pass

    def get_king_moves(self):
        return self.possible_moves[0:8]

    def get_pawn_attack_moves(self):
        return self.possible_moves[1:3]

    def promote_pawn(self):
        color = self.color
        x_file = self.x_file
        y_file = self.y_file
        del self
        return Piece(x_file, y_file, color, "Q")
