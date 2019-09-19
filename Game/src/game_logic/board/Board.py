from game_logic.pieces.Piece import Piece
from config.Config import Config as cfg
import pygame
import numpy as np


class Board:
    white_pieces = []
    black_pieces = []
    current_player = "white"
    chessboard = []
    turn = 1
    is_checked = [False, False]  # index 0 for white, index 1 for black

    def __init__(self):

        # board image
        self.image_path = "media/boards/board_1.jpg"
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (cfg.display_width, cfg.display_height))

        self.has_selected_piece = False

        for i in range(8):
            self.chessboard.append([])
            for j in range(8):
                self.chessboard[i].append("*")

        # piece configuration
        board_setup = open("config/board_setup.txt")
        for j in range(8):
            current_line = board_setup.readline()
            for i in range(8):
                if current_line[i] == "*":
                    self.chessboard[i].append(None)
                    continue
                elif current_line[i] == "k":
                    current = Piece(i, j, "black", "K")
                    self.black_pieces.append(current)
                    self.chessboard[i].append(current)
                elif current_line[i] == "q":
                    current = Piece(i, j, "black", "Q")
                    self.black_pieces.append(current)
                    self.chessboard[i].append(current)
                elif current_line[i] == "r":
                    current = Piece(i, j, "black", "R")
                    self.black_pieces.append(current)
                    self.chessboard[i].append(current)
                elif current_line[i] == "b":
                    self.black_pieces.append(Piece(i, j, "black", "B"))
                elif current_line[i] == "n":
                    self.black_pieces.append(Piece(i, j, "black", "N"))
                elif current_line[i] == "p":
                    self.black_pieces.append(Piece(i, j, "black", "P"))
                elif current_line[i] == "K":
                    self.white_pieces.append(Piece(i, j, "white", "K"))
                elif current_line[i] == "Q":
                    self.white_pieces.append(Piece(i, j, "white", "Q"))
                elif current_line[i] == "R":
                    self.white_pieces.append(Piece(i, j, "white", "R"))
                elif current_line[i] == "B":
                    self.white_pieces.append(Piece(i, j, "white", "B"))
                elif current_line[i] == "N":
                    self.white_pieces.append(Piece(i, j, "white", "N"))
                elif current_line[i] == "P":
                    self.white_pieces.append(Piece(i, j, "white", "P"))

    def detect_check(self):
        # WHITE KING
        pieces = self.black_pieces
        for piece in self.white_pieces:
            if piece.TYPE == "K":
                king = piece
                break;
        for piece in pieces:
            x_difference = king.x_file - piece.x_file
            y_difference = piece.y_file - king.y_file
            if [x_difference, y_difference] in piece.possible_moves:
                if not self.has_obstacles(king.x_file, king.y_file, x_difference, y_difference, piece):
                    self.is_checked[0] = True
                    break
            self.is_checked[0] = False
        print("beyaza check yok")
        # BLACK KING

        pieces = self.white_pieces
        for piece in self.black_pieces:
            if piece.TYPE == "K":
                king = piece
                break;
        for piece in pieces:
            x_difference = king.x_file - piece.x_file
            y_difference = piece.y_file - king.y_file
            if [x_difference, y_difference] in piece.possible_moves:
                if not self.has_obstacles(king.x_file, king.y_file, x_difference, y_difference, piece):
                    self.is_checked[1] = True
                    break
            self.is_checked[1] = False
        print("siyaha check yok")

    def get_piece_by_position(self, x, y):
        for piece in self.white_pieces + self.black_pieces:
            if piece.x_file == x and piece.y_file == y:
                return piece
        return None

    def remove_piece_by_position(self, x, y, color):
        if color == "black":
            for piece in self.white_pieces:
                if piece.x_file == x and piece.y_file == y:
                    self.white_pieces.remove(piece)
                    return True
        else:
            for piece in self.black_pieces:
                if piece.x_file == x and piece.y_file == y:
                    self.black_pieces.remove(piece)
                    return True
        return False

    def has_obstacles(self, x, y, x_difference, y_difference, piece):
        if self.current_player == "white":
            pieces = self.white_pieces
        else:
            pieces = self.black_pieces

        has_obstacle = False
        if piece.TYPE != "N" and piece.TYPE != "K":
            possible_move_vector = [0, 0]
            if x_difference != 0:
                possible_move_vector[0] = int(x_difference / abs(x_difference))
            if y_difference != 0:
                possible_move_vector[1] = int(y_difference / abs(y_difference))
            possible_move_vector_original = possible_move_vector
            while possible_move_vector != [x_difference, y_difference]:
                if self.get_piece_by_position(piece.x_file + possible_move_vector[0],
                                              piece.y_file - possible_move_vector[1]) is not None:
                    has_obstacle = True
                    break
                possible_move_vector = np.add(possible_move_vector, possible_move_vector_original).tolist()
        for obstacle in pieces:
            if obstacle.x_file == x and obstacle.y_file == y:
                has_obstacle = True
                break
        if has_obstacle:
            return True
        else:
            return False

    def move_piece(self, x, y):
        if self.current_player == "white":
            pieces = self.white_pieces
        else:
            pieces = self.black_pieces

        self.detect_check()

        for piece in pieces:
            if piece.is_selected:
                x_difference = x - piece.x_file
                y_difference = piece.y_file - y

                if [x_difference, y_difference] in piece.possible_moves:
                    ##### CHECK OBSTACLES
                    if self.has_obstacles(x, y, x_difference, y_difference, piece):
                        piece.is_selected = False
                        self.has_selected_piece = False
                        return

                    #### PAWN SPECIAL MOVES
                    if piece.TYPE == "P":
                        if [x_difference, y_difference] in piece.get_pawn_attack_moves():
                            if not self.remove_piece_by_position(x, y, piece.color):
                                piece.is_selected = False
                                self.has_selected_piece = False
                                return False
                        else:
                            if self.get_piece_by_position(x, y) is None:
                                if (piece.color == "white" and piece.y_file == 6) or (
                                        piece.color == "black" and piece.y_file == 1):
                                    piece.update_pawn_first_move()
                            else:
                                piece.is_selected = False
                                self.has_selected_piece = False
                                return False
                    ##########
                    ##
                    ### ROOK
                    elif piece.TYPE == "K" and (
                            [x_difference, y_difference] not in piece.get_king_moves() and [x_difference,
                                                                                            y_difference] in piece.possible_moves):
                        print("ben fero")
                        if x == 1:
                            piece_in_castle_loc = self.get_piece_by_position(0, y)
                        elif x == 6:
                            piece_in_castle_loc = self.get_piece_by_position(7, y)
                        else:
                            piece_in_castle_loc = None

                        if piece_in_castle_loc is not None:
                            print("king kong")
                            if piece_in_castle_loc.TYPE == "R" and (piece.color == piece_in_castle_loc.color):
                                print("zing zong")
                                if piece_in_castle_loc.x_file == 0:
                                    piece_in_castle_loc.x_file = 2
                                else:
                                    piece_in_castle_loc.x_file = 5
                            piece.castle_not_possible()

                        else:
                            return False
                    ########
                    else:
                        self.remove_piece_by_position(x, y, piece.color)

                    """"""""
                    print(piece.TYPE, "~", [x_difference, y_difference], "~", piece.get_king_moves(), "~",
                          piece.possible_moves)
                    """"""""
                    piece.x_file = x
                    piece.y_file = y
                    if piece.TYPE == "K":
                        print("hebele")
                        piece.castle_not_possible()
                    #### Promotion
                    if piece.TYPE == "P":
                        if piece.color == "black" and piece.y_file == 7:
                            temp_piece = piece
                            self.black_pieces.remove(piece)
                            self.black_pieces.append(piece.promote_pawn())
                            temp_piece.is_selected = False
                            self.has_selected_piece = False
                            self.turn += 1
                            if self.current_player == "white":
                                self.current_player = "black"
                            else:
                                self.current_player = "white"
                            return
                        if piece.color == "white" and piece.y_file == 0:
                            temp_piece = piece
                            self.white_pieces.remove(piece)
                            self.white_pieces.append(piece.promote_pawn())
                            temp_piece.is_selected = False
                            self.end_turn()
                            return

                    ####

                    piece.is_selected = False
                    self.end_turn()
                    return

    def select_piece(self, x, y):
        if self.current_player == "white":
            pieces = self.white_pieces
        else:
            pieces = self.black_pieces
        for piece in pieces:
            if x == piece.x_file and y == piece.y_file and not self.has_selected_piece:
                piece.is_selected = True
                self.has_selected_piece = True
                return

    def end_turn(self):
        self.has_selected_piece = False
        self.turn += 1
        if self.current_player == "white":
            self.current_player = "black"
        else:
            self.current_player = "white"
