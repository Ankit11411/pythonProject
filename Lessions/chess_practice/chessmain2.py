import pygame as p

HEIGHT = WIDTH = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
IMAGES = {}
BOARD = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
]

def drawBoard(screen):
    colors = [p.Color('white'), p.Color('gray')]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            p.draw.rect(screen, colors[(row + col) % 2], p.Rect(row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = BOARD[row][col]
            if piece != '--':
                screen.blit(IMAGES[piece], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def makeMove(pos1,pos2):
    pieceMove = BOARD[pos1[0]][pos1[1]]
    BOARD[pos1[0]][pos1[1]] = '--'
    BOARD[pos2[0]][pos2[1]] = pieceMove

def main():
    pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bR", "bN", "bB", "bK", "bQ"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    screen = p.display.set_mode((HEIGHT, WIDTH))
    screen.fill(color='white')
    playLog = []
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                row = location[0] // SQ_SIZE
                col = location[1] // SQ_SIZE
                sqSelect = (col, row)
                print(sqSelect,playLog)
                playLog.append(sqSelect)
                if BOARD[playLog[0][0]][playLog[0][1]] == '--':
                    playLog = []
                if len(playLog) == 2:
                    print(playLog)
                    makeMove(playLog[0],playLog[1])
                    playLog = []
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    print("ASD")

        drawBoard(screen)
        drawPieces(screen)
        p.display.update()


if __name__ == '__main__':
    main()
