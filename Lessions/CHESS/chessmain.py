import pygame as p
from Lessions.CHESS import chessengine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bR", "bN", "bB", "bK", "bQ"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    p.init()
    p.font.init()
    p.mixer.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = chessengine.GameState()
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []
    validMoves = gs.getValidMoves()
    moveMade = False

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            # Mouse Handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                makeSound(row,col,gs)


                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)

                if len(playerClicks) == 2:
                    move = chessengine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    print(playerClicks)
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                    sqSelected = ()
                    playerClicks = []

            # Key HAndler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
                    sqSelected = ()
                    playerClicks = []



        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False


def drawGameState(screen, gs):
    drawBoard(screen)

    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [p.Color('gray50'), p.Color('gray90')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def makeSound(row,col,gs):
    gs.makeSound(row,col,gs)


if __name__ == "__main__":
    main()
