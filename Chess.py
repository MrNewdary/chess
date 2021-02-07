import pygame

pygame.init()


class ChessPiece:
    def __init__(self, colour, x, y, image):
        self.colour = colour
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.alive = True

    def draw(self, surface):
        image_sized = pygame.transform.scale(self.image, (50, 50))
        surface.blit(image_sized, (50*self.x + (750//2)-4*50, 50*self.y + (750//2)-4*50))
        pass

    def is_over(self, pos):
        if (50*self.x+(750//2)-4*50) < pos[0] < (50*self.x+(750//2)-4*50) + 50:
            if (50*self.y+(750//2)-4*50) < pos[1] < (50*self.y+(750//2)-4*50) + 50:
                return True

    def in_bounds(self):
        pass

        return False


class ChessBoard:
    def __init__(self):
        pass

    @staticmethod
    def draw():
        for i in range(8):
            for j in range(8):
                if (j + (9*i)) % 2 == 0:
                    colour = (255, 255, 255)
                else:
                    colour = (210, 105, 30)
                pygame.draw.rect(win, colour, (50*j + (750//2)-4*50, 50*i + (750//2)-4*50, 50, 50), 0)


class Pawn(ChessPiece):
    def __init__(self, colour, x, y, image):
        super().__init__(colour, x, y, image)

    def legal_moves(self):
        moves = []
        return moves


class Knight(ChessPiece):
    def __init__(self, colour, x, y, image):    
        super().__init__(colour, x, y, image)

    def legal_moves(self):
        moves = []
        return moves


class Bishop(ChessPiece):
    def __init__(self, colour, x, y, image):
        super().__init__(colour, x, y, image)

    def legal_moves(self):
        moves = []
        return moves


class Rook(ChessPiece):
    def __init__(self, colour, x, y, image):
        super().__init__(colour, x, y, image)

    def legal_moves(self):
        moves = []
        return moves


class Queen(ChessPiece):
    def __init__(self, colour, x, y, image):
        super().__init__(colour, x, y, image)

    def legal_moves(self):
        moves = []
        return moves


class King(ChessPiece):
    def __init__(self, colour, x, y, image):
        super().__init__(colour, x, y, image)

    def legal_moves(self):
        moves = []
        return moves

    def under_check(self):
        pass

    def under_checkmate(self):
        pass


def redraw_window():
    win.fill((0, 255, 0))
    board.draw()
    for piece in Pieces:
        piece.draw(win)


def main():
    global win
    global board
    clock = pygame.time.Clock()
    board = ChessBoard()
    win = pygame.display.set_mode((750, 750))
    run = True
    while run:
        pygame.event.get()
        pygame.time.delay(50)
        clock.tick(10)
        redraw_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

Pieces = [
    Pawn('white', 0, 6, "white_pawn.png"),
    Pawn('white', 1, 6, "white_pawn.png"),
    Pawn('white', 2, 6, "white_pawn.png"),
    Pawn('white', 3, 6, "white_pawn.png"),
    Pawn('white', 4, 6, "white_pawn.png"),
    Pawn('white', 5, 6, "white_pawn.png"),
    Pawn('white', 6, 6, "white_pawn.png"),
    Pawn('white', 7, 6, "white_pawn.png"),
    Rook('white', 0, 7, "white_rook.png"),
    Rook('white', 7, 7, "white_rook.png"),
    Knight('white', 1, 7, "white_knight.png"),
    Knight('white', 6, 7, "white_knight.png"),
    Bishop('white', 2, 7, "white_bishop.png"),
    Bishop('white', 5, 7, "white_bishop.png"),
    Queen('white', 3, 7, "white_queen.png"),
    King('white', 4, 7, "white_king.png"),
    Pawn('black', 0, 1, "black_pawn.png"),
    Pawn('black', 1, 1, "black_pawn.png"),
    Pawn('black', 2, 1, "black_pawn.png"),
    Pawn('black', 3, 1, "black_pawn.png"),
    Pawn('black', 4, 1, "black_pawn.png"),
    Pawn('black', 5, 1, "black_pawn.png"),
    Pawn('black', 6, 1, "black_pawn.png"),
    Pawn('black', 7, 1, "black_pawn.png"),
    Rook('black', 0, 0, "black_rook.png"),
    Rook('black', 7, 0, "black_rook.png"),
    Knight('black', 1, 0, "black_knight.png"),
    Knight('black', 6, 0, "black_knight.png"),
    Bishop('black', 2, 0, "black_bishop.png"),
    Bishop('black', 5, 0, "black_bishop.png"),
    Queen('black', 3, 0, "black_queen.png"),
    King('black', 4, 0, "black_king.png")
]


if __name__ == '__main__':
    main()
